import ida_idaapi
import ida_funcs
import idautils

'''
The modern plugin framework simplifies plugin development.
A plugin should:
* flags should include PLUGIN_MULTI
* subclass plugmod_t
* override plugmod_t::run() virtual method
* term() callback should no longer be used
* plugon_t's init()) callback return a new instance of the plugmod_t subclass
'''

class MyPlugmod(ida_idaapi.plugmod_t):
    def __del__(self):
        print(">>> MyPlugmod: destructor called.")
    
    def run(self, arg):
        print(">>> MyPlugmod.run() is invoked with argument value: {arg}.")
        for func_ea in idautils.Functions():
            func_name = ida_funcs.get_func_name(func_ea)
            print(f">>>MyPlugmod: Function{func_name} at address {func_ea:x}")


class MyPlugin(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_UNL | ida_idaapi.PLUGIN_MULTI
    comment = "This is my first simple IDA Pro plugin"
    help = "This plugin lists all functions in the current database"
    wanted_name = "My First Plugin"
    wanted_hotkey = "Shift-P"

    def init(self):
        print(">>>MyPlugin: Init called.")
        return MyPlugmod()


def PLUGIN_ENTRY():
    return MyPlugin()