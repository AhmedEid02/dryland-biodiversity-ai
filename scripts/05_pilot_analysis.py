from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(".")
OUT = ROOT / "outputs"
FIG = ROOT / "figures"

FIG.mkdir(exist_ok=True)

species = pd.read_csv(OUT / "pilot_species_summary.csv")
images = pd.read_csv(OUT / "pilot_image_summary.csv")

# Species performance figure
species = species.sort_values("direct_accuracy")

y = range(len(species))

fig, ax = plt.subplots(figsize=(9, 6))

ax.barh(
    [i - 0.18 for i in y],
    species["direct_accuracy"],
    height=0.36,
    label="Direct classification"
)

ax.barh(
    [i + 0.18 for i in y],
    species["pipeline_success"],
    height=0.36,
    label="Detector -> classifier"
)

ax.set_yticks(list(y))
ax.set_yticklabels(species["species"])

ax.set_xlim(0, 105)
ax.set_xlabel("Image-level success (%)")
ax.set_ylabel("Species")

ax.set_title(
    "Dryland Biodiversity AI Pilot:\n"
    "Direct Classification vs Detector-Classifier Pipeline"
)

ax.legend(frameon=False)

for i, (_, row) in enumerate(species.iterrows()):

    ax.text(
        row["direct_accuracy"] + 1,
        i - 0.18,
        f'{row["direct_accuracy"]:.0f}%',
        va="center",
        fontsize=8
    )

    ax.text(
        row["pipeline_success"] + 1,
        i + 0.18,
        f'{row["pipeline_success"]:.0f}%',
        va="center",
        fontsize=8
    )

plt.tight_layout()

plt.savefig(
    FIG / "pilot_species_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    FIG / "pilot_species_performance.pdf",
    bbox_inches="tight"
)

plt.close()


# Failure diagnostic table
failures = images[
    (~images["direct_correct"]) |
    (~images["pipeline_correct"])
].copy()

failures["outcome"] = "Failed in both"

failures.loc[
    (~failures["direct_correct"]) &
    (failures["pipeline_correct"]),
    "outcome"
] = "Recovered by pipeline"

failures.loc[
    (failures["direct_correct"]) &
    (~failures["pipeline_correct"]),
    "outcome"
] = "Lost after pipeline"

failures[
    [
        "image_id",
        "true_class",
        "direct_prediction",
        "direct_correct",
        "pipeline_correct",
        "pipeline_animal_detections",
        "outcome"
    ]
].to_csv(
    OUT / "pilot_failure_diagnostics.csv",
    index=False
)


# Console summary
print("=== PILOT DIAGNOSTIC SUMMARY ===")
print()

print("Species tested:", len(species))
print("Images tested:", len(images))

print()
print("Recovered by detector-classifier pipeline:")

recovered = failures[
    failures["outcome"] == "Recovered by pipeline"
]

if len(recovered):
    for _, row in recovered.iterrows():
        print(
            f"  {row['image_id']}: "
            f"{row['true_class']} "
            f"(direct predicted {row['direct_prediction']})"
        )
else:
    print("  None")

print()
print("Failed in both workflows:")

both_failed = failures[
    failures["outcome"] == "Failed in both"
]

for _, row in both_failed.iterrows():
    print(
        f"  {row['image_id']}: "
        f"{row['true_class']} "
        f"(direct predicted {row['direct_prediction']})"
    )

print()
print("Created:")
print("  figures/pilot_species_performance.png")
print("  figures/pilot_species_performance.pdf")
print("  outputs/pilot_failure_diagnostics.csv")
