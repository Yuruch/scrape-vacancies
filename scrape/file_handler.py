import csv
import os
from typing import List

from tqdm import tqdm

from config import RESULT_DIR


class FileWriter:
    @staticmethod
    def write_csv(data: List[dict], category: str) -> None:
        filename = os.path.join(RESULT_DIR, f"{category}_jobs.csv")

        with open(filename, mode="w", newline="") as file:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            file.seek(0, 2)
            if file.tell() == 0:
                writer.writeheader()

            for job in tqdm(data, desc="Saving jobs to CSV"):
                writer.writerow(job)
