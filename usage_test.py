from GUIMonkey import GUIMonkey

CLO_PATH = f"foo/bar.exe"

gm = GUIMonkey()

clo_test = gm.new_timeline(CLO_PATH)
clo_test.add_step()



clo_test.run_timeline()
