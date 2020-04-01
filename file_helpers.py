
import os
import random
import string

class FileHelpers:

    @staticmethod
    def get_or_create_folder():
        cur_dir = os.path.abspath(os.getcwd())
        req_dir = os.path.join(cur_dir, "template_models")
        if not os.path.exists(req_dir):
            os.makedirs(req_dir)

        temp_folder_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        cur_temp_folder = os.path.join(req_dir, temp_folder_name)
        os.makedirs(cur_temp_folder)

        return cur_temp_folder
