import execjs

with open('node.js', 'r') as f:
    node_js = f.read()
execjs_obj = execjs.compile(node_js)
result = execjs_obj.eval('e("kit")')
print(result)
