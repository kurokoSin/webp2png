import io
import os
from PIL import Image
import zipfile

class Webp2Png:
    @staticmethod
    def controller(zip_path):
        dest_path = Webp2Png.create_png_directory(zip_path)
        Webp2Png.trans_to_pngs(zip_path, dest_path)
        pass

    @staticmethod
    def create_png_directory(zip_path):
        dest_path = os.path.dirname(zip_path) 
        dir_name = os.path.splitext(os.path.basename(zip_path))[0]
        dest_path = os.path.join(dest_path, f'{dir_name}_png')
        is_exist = os.path.exists(dest_path)
        if not is_exist :
            os.makedirs(dest_path)
        return dest_path

    @staticmethod
    def trans_to_pngs(zip_path, dest_path):
        with zipfile.ZipFile(zip_path, 'r') as zf:
            for info in zf.infolist():
                # print(f'（{str(info.file_size)}） {info.filename}')
                basename = os.path.splitext(os.path.basename(info.filename))[0]
                transed_name = os.path.join(dest_path, f'{basename}.png')
                with zf.open(info.filename) as fp:
                    webp = io.BytesIO(fp.read())
                    im = Image.open(webp).convert('RGB')
                    im.save(transed_name, 'png')
                    

                
        return zip_path
