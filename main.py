from gen import *
from find import *
from select_file import *
from VtestStudioToAtesyReportRevisedForPy3 import *
import frozen_dir
import sys

SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)

try:
    file_path, target_dir = get_paths()

    # read from the config file
    conf = read_config(os.path.join(SETUP_DIR, "config", "conf.yaml"))
    id_to_name = conf["id_to_name"]
    atesy_template_header = conf["atesy_template_header"]
    atesy_template_testcase = conf["atesy_template_testcase"]
    atesy_template_tail = conf["atesy_template_tail"]

    cont = open_xml(file_path)
    parsed = parse_test_cases(cont)
    tc_dic, type_id = generate_dic_and_decide_type(parsed)

    folder_name = id_to_name[type_id]

    folder_dir = create_folder(target_dir, folder_name)

    # default template is the template in the current directory
    template_content = read_from_template(os.path.join(SETUP_DIR, "temp", "Template.py"))

    for k, v in tc_dic.items():
        f_path = create_py(folder_dir, k)
        edit_content(f_path, template_content, k, v)

    print("Waiting for setting to create XML file...")

    ori_file_path, new_target_dir = further_procedure_path(file_path)
    original_file_name = ori_file_path.split("\\")[-1]
    create_atesy(ori_file_path, os.path.join(new_target_dir, "aTeSy_" + original_file_name), atesy_template_header, atesy_template_tail, atesy_template_testcase)

except KeyError:
    print("[Error] The ID of test cases is not valid.")
except FileNotFoundError:
    print("[Error] Directories cannot be empty. Check Again!")
except UnicodeDecodeError:
    print("[Error] Wrong file format. Check Again!")
except TypeError:
    pass

input("Press Enter to exit...")
