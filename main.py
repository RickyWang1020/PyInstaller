from gen import *
from find import *
from select_file import *
from VtestStudioToAtesyReportRevisedForPy3 import *
import frozen_dir
import sys

SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)

try:
    file_path, target_dir, to_create_folder, to_gen_xml = check_box()

    if to_create_folder or to_gen_xml:

        conf = read_config("conf.yaml")
        cont = open_xml(file_path)
        parsed = parse_test_cases(cont)
        tc_dic, type_id = generate_dic_and_decide_type(parsed)

        if to_create_folder:
            id_to_name = conf["id_to_name"]
            folder_name = id_to_name[type_id]

            folder_dir = create_folder(target_dir, folder_name)

            # default template is the template in the current directory
            template_content = read_from_template("Template.py")

            for k, v in tc_dic.items():
                f_path = create_py(folder_dir, k)
                edit_content(f_path, template_content, k, v)

        if to_gen_xml:
            atesy_template_header = conf["atesy_template_header"]
            atesy_template_testcase = conf["atesy_template_testcase"]
            atesy_template_tail = conf["atesy_template_tail"]

            original_file_name = file_path.split("\\")[-1]
            create_atesy(file_path, os.path.join(target_dir, "aTeSy_" + original_file_name), atesy_template_header, atesy_template_tail, atesy_template_testcase)
    else:
        print("You didn't select any data processing option...")

except KeyError:
    print("[Error] The ID of test cases is not valid.")
except FileNotFoundError:
    print("[Error] Directories cannot be empty. Check Again!")
except UnicodeDecodeError:
    print("[Error] Wrong file format. Check Again!")
except TypeError:
    pass

input("Press Enter to exit...")
