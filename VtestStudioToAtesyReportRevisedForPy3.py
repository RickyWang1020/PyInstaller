from xml.etree import ElementTree as ET
import re as _re
cnt = 0
############################################
def walkData(root_node, level, env, to_write, template_testcase):
    # 找出运行环境
    global cnt
    if root_node.tag == "testunit":
        env = root_node.find("title").text
    # 找出结果
    if root_node.tag == "testcase": 
        description = root_node.find("title").text
        status = root_node.find("verdict").get("result")
        if status == "none": # 未运行测试导致的结果空项无需计入
            pass
        else:
            cnt += 1
            if _re.match(r"tc\d\d\d(?:_\d\d\d){2,3}", description):
                # 如果testcase title是 tcxxx_xxx_xxx: description或tcxxx_xxx_xxx_xxx格式
                unique_id = description[:description.find(":")]
                description = description[description.find(":")+2:]
                print("Processing:")
                print(unique_id) # test ID
                print(description) # description is the test purpose
                print(status) # status is the result e.g. pass and fail
                print(env) # environment is the test environment such as SAIC AP3X, SAIC ER31
                print()
                to_write.writelines(template_testcase % (unique_id, description, status))
            else:
                # 如果testcase title 只有描述 没有序号
                print("Processing:")
                print(cnt) # cnt is the test ID
                print(description) # description is the test purpose
                print(status) # status is the result e.g. pass and fail
                print(env) # environment is the test environment such as SAIC AP3X, SAIC ER31
                print()
                to_write.writelines(template_testcase % (cnt, description, status))
    # 递归遍历每个子节点
    children_node = list(root_node.getchildren())
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, env, to_write, template_testcase)
    return

def getXmlData(file_name, env, write_tmp, template_testcase):
    level = 1 # 节点的深度从1开始
    root = ET.parse(file_name).getroot()
    walkData(root, level, env, write_tmp, template_testcase)
    return

##################### Main ########################
def create_atesy(sourcefile, releasefile, template_header, template_tail, template_testcase):
    print("Processing... ")
    #Create file
    print("\nBuilding atesy_template_header")
    writeTmp = open(releasefile, 'w')
    writeTmp.writelines(template_header)
    print("Done.")
    print("\nBuilding atesy_template_testcase")

    environment = "Project"
    R = getXmlData(sourcefile, environment, writeTmp, template_testcase)

    print("Done.")

    print("\nBuilding atesy_template_tail")
    writeTmp.writelines(template_tail % environment)
    writeTmp.close()
    print("Done.")

    print("\nSucceed in build file: " + releasefile)
