from pathlib import Path
import shutil


class Images_Preprocessing:
    def get_img_paths(self, data_path: Path, supp_ext: list[str]) -> list[Path]:
        return [
            path
            for path in data_path.rglob("*")
            if path.is_file() and path.suffix.lower() in supp_ext
        ]

    def change_path(
        self, old_file_path: Path, folder_name_to_change: str, new_folder_name: str
    ) -> Path:
        parts = list(old_file_path.parts)
        if folder_name_to_change in parts:
            index = parts.index(folder_name_to_change)
            parts[index] = new_folder_name
            return Path(*parts)
        else:
            raise ValueError(folder_name_to_change, " not in ", old_file_path)

    def copy_images(self, data_path: Path, image_extensions: list[str]) -> None:
        old_imgs_paths = self.get_img_paths(data_path, image_extensions)

        for file_path in old_imgs_paths:
            new_img_file_path = self.change_path(
                file_path, "unziped-ua-detrac", "images"
            )
            new_img_file_path = self.change_path(new_img_file_path, "raw", "processed")
            new_img_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, new_img_file_path)
