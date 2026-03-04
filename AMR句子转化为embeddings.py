import re
cleaned_line=":arg1(x4/因) (x5_x7 / 做完-01   :arg0-of() (x8 / 恶劣-01)))"
role_pattern = re.compile(r'(:\w+(-of)?)')
# 匹配当前行所有语义角色，返回列表（如[(":ARG0", ""), (":ARG1-of", "-of")]）
role_matches = [match[0] for match in role_pattern.findall(cleaned_line)]
print(role_matches)
xid_pattern = re.compile(r'x(\d+)')
# 匹配当前行所有x_id的数字部分（如x7 x9 → ["7", "9"]）
xid_matches = xid_pattern.findall(cleaned_line)
# 无x_id则返回空列表
# 生成完整x_id列表（共节点x_id组）：如["7", "9"] → ["x7", "x9"]
xid_group = [f"x{num}" for num in xid_matches]
print(xid_group)
# 步骤3：提取每个x_id对应的token（共节点token组）
token_group = []
# 遍历x_id组中的每个x_id
for x_id in xid_group:
    current_token_pattern = re.compile(rf'{re.escape(x_id)}\s*/\s*([^)\s]+)')
# 匹配当前行中该x_id的token
    current_matches = current_token_pattern.findall(cleaned_line)
    print(current_matches)