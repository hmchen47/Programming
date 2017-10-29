Python in GDB
-------------

# two ways to use
```python
python
import os
print("my pid is {:d}".format(os.getpid()))
end
```

# useful built-in methods
```gdb
python bp = gdb.Breakpoint("hello.c:17")

python gdb.execute('next')
python gdb.parse_and_eval()
python help('gdb')
python help('gdb.Breakpoint')

python bps = gdb.breakpoints()
```

# usage
```GDB
python var_i = gdb.parse_and_eval('i')
# var_i is not integer, before print, need run the above command
python print("var_i = %d" % var_i)
python print("var_i is {}".format(var_i))
```

# Python Pretty printer -
```python
python

class MyPrinter(object):
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return (self.val['member'])

import gdb.printing
pp = gdb.printing.RegexpCollectionPrettyPrinter('mystruct')
pp.add_printer('mystruct', '^mystruct$', MyPrinter)
gdb.printing.register_pretty_printer(gdb.current_objfile(), pp)

end
```
- execute 'gdb structs' and runn a couple lines
```gdb
(gdb) print st
$1 = {id = 123, name = 0x602010 "Jon Doe", dob = {tm_sec = 0, tm_min = 30, tm_hour = 9, tm_mday = 2, tm_mon = 9, tm_year = 100, tm_wday = 0, tm_yday = 0, tm_isdst = 0, tm_gmtoff = 0, tm_zone = 0x0}}


(gdb) __set print pretty on__
(gdb) p st
$2 = {
  id = 123,
  name = 0x602010 "Jon Doe",
  dob = {
    tm_sec = 0,
    tm_min = 30,
    tm_hour = 9,
    tm_mday = 2,
    tm_mon = 9,
    tm_year = 100,
    tm_wday = 0,
    tm_yday = 0,
    tm_isdst = 0,
    tm_gmtoff = 0,
    tm_zone = 0x0

(gdb) call dump_student(&st)
id: 123
name: Jon Doe
dob: (0x7ffff7dd39c0) Sun Oct  2 09:30:00 2000

(gdb) source pretty.py
(gdb) p st
$1 = month = 9
id = 123 name=0x602010 "Jon Doe" dob='Mon Sep  2 09:30:00 2000'

```

# reverseible debugging
```
hmchen@freby01:cppcon2015$ while ./bubble; do echo OK; done
*** stack smashing detected ***: ./bubble terminated
Aborted (core dumped) --> unable to reproduce the segmentation fault

gdb -c core --> debug with the core dump
(gdb) print $pc --> program counter
$1 = (void (*)()) 0x5a4f3c99
(gdb) x $1
0x5a4f3c99:     Cannot access memeory at address 0x5a4f3c99  ==> not working
(gdb) bt ==> traceback command but no useful info
```

- reverse debugging

commands -- Set commands to be executed when a breakpoint is hit

```
# execute the program
(gdb) start
Temporary breakpoint 1 at 0x4006cc: file bubble_sort.c, line 41.
Starting program: /home/hmchen/Projects/Programming/C_C++/misc/cppcon2015/bubble

Temporary breakpoint 1, main () at bubble_sort.c:41
41	{

# set breakpoint 2
(gdb) b main
Breakpoint 2 at 0x4006cc: file bubble_sort.c, line 41.

# set breakpoint 3
(gdb) b _exit
Breakpoint 3 at 0x7ffff7ad9b60: file ../sysdeps/unix/sysv/linux/_exit.c, line 27.

# define the commands when hit breakpoint 2 --> record the process for backtrace
(gdb) commands 2
Type commands for breakpoint(s) 2, one per line.
End with a line saying just "end".
>record
>continue
>end

# define the commands when hits breakpoint 3 --> rerun the program
(gdb) commands 3
Type commands for breakpoint(s) 3, one per line.
End with a line saying just "end".
>run
>end
```

## issue encountered
```
Breakpoint 2, main () at bubble_sort.c:41
41	{
Process record does not support instruction 0xc5 at address 0x7ffff7dee6e7.
Process record: failed to record execution log.

Program stopped.
_dl_runtime_resolve_avx () at ../sysdeps/x86_64/dl-trampoline.h:81
81	../sysdeps/x86_64/dl-trampoline.h: No such file or directory.
```

## follow the instruction from demo
+ once the program terminated
```
(gdb) bt --> list of

(gdb) reverse-stepi -> reverse one step with machine instruction
==> get the last exit line of the souorce code

c-x + a ==> launch TUI
(gdb) print $sp ==> stack pointer
(gdb) x $l ==> display the content of the address 0x7ffffffd9e8: 0x7b6b3273
(gdb) x/8 $l ==> display 8 bytes
(gdb) print *(long**) 0x7ffffffd9e8 ==> $2 = (long *) 0x7b6b3273
(gdb) x $2 ==> Cannot access memory at address 0x7b6b3273
(gdb) watch *(long**) 0x7ffffffd9e8 ==> Hardware watchpoint 4: *(long**) 0x7ffffffd9e8
(gdb) revers-continue ==> run prorogram reversed
(gdb) print i ==> $3 = 33
(gdb) whatis array ==> type = long [32]
(gdb) print sizeof array ==> $4 = 256
```


# python help(gdb)

NAME
    gdb - # Copyright (C) 2010-2016 Free Software Foundation, Inc.

PACKAGE CONTENTS
    FrameDecorator
    FrameIterator
    command (package)
    frames
    function (package)
    printer (package)
    printing
    prompt
    types
    unwinder
    xmethod

SUBMODULES
    events

CLASSES
    builtins.Exception(builtins.BaseException)
        GdbError
    builtins.RuntimeError(builtins.Exception)
        error
            MemoryError
    builtins.object
        Architecture
        Block
        BlockIterator
        Breakpoint
            FinishBreakpoint
        Command
        Event
            ClearObjFilesEvent
            ExitedEvent
            InferiorCallPostEvent
            InferiorCallPreEvent
            MemoryChangedEvent
            NewObjFileEvent
            RegisterChangedEvent
            ThreadEvent
                ContinueEvent
                StopEvent
                    BreakpointEvent
                    SignalEvent
        EventRegistry
        Field
        Frame
        Function
        Inferior
        InferiorThread
        LineTable
        LineTableEntry
        LineTableIterator
        Membuf
        Objfile
        Parameter
        PendingFrame
        Progspace
        Symbol
        Symtab
        Symtab_and_line
        Type
        TypeIterator
        UnwindInfo
        Value
    _GdbFile(builtins.object)
        GdbOutputErrorFile
        GdbOutputFile

    class Architecture(builtins.object)
     |  GDB architecture object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  disassemble(...)
     |      disassemble (start_pc [, end_pc [, count]]) -> List.
     |      Return a list of at most COUNT disassembled instructions from START_PC to
     |      END_PC.
     |
     |  name(...)
     |      name () -> String.
     |      Return the name of the architecture as a string value.

    class Block(builtins.object)
     |  GDB block object
     |
     |  Methods defined here:
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this block is valid, false if not.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  end
     |      End address of the block.
     |
     |  function
     |      Symbol that names the block, or None.
     |
     |  global_block
        Objfile
        Parameter
        PendingFrame
        Progspace
        Symbol
        Symtab
        Symtab_and_line
        Type
        TypeIterator
        UnwindInfo
        Value
    _GdbFile(builtins.object)
        GdbOutputErrorFile
        GdbOutputFile

    class Architecture(builtins.object)
     |  GDB architecture object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  disassemble(...)
     |      disassemble (start_pc [, end_pc [, count]]) -> List.
     |      Return a list of at most COUNT disassembled instructions from START_PC to
     |      END_PC.
     |
     |  name(...)
     |      name () -> String.
     |      Return the name of the architecture as a string value.

    class Block(builtins.object)
     |  GDB block object
     |
     |  Methods defined here:
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this block is valid, false if not.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  end
     |      End address of the block.
     |
     |  function
     |      Symbol that names the block, or None.
     |
     |  global_block
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  commands
     |      Commands of the breakpoint, as specified by the user.
     |
     |  condition
     |      Condition of the breakpoint, as specified by the user,or None if no condition set.
     |
     |  enabled
     |      Boolean telling whether the breakpoint is enabled.
     |
     |  expression
     |      Expression of the breakpoint, as specified by the user.
     |
     |  hit_count
     |      Number of times the breakpoint has been hit.
     |      Can be set to zero to clear the count. No other value is valid
     |      when setting this property.
     |
     |  ignore_count
     |      Number of times this breakpoint should be automatically continued.
     |
     |  location
     |      Location of the breakpoint, as specified by the user.
     |
     |  number
     |      Breakpoint's number assigned by GDB.
     |
     |  silent
     |      Boolean telling whether the breakpoint is silent.
     |
     |  task
     |      Thread ID for the breakpoint.
     |      If the value is a task ID (integer), then this is an Ada task-specific breakpoint.
     |      If the value is None, then this breakpoint is not task-specific.
     |      No other type of value can be used.
     |
     |  temporary
     |      Whether this breakpoint is a temporary breakpoint.
     |
     |  thread
     |      Thread ID for the breakpoint.
     |      If the value is a thread ID (integer), then this is a thread-specific breakpoint.
     |      If the value is None, then this breakpoint is not thread-specific.
     |      No other type of value can be used.
     |
     |  type
     |      Type of breakpoint.
     |
     |  visible
     |      Whether the breakpoint is visible to the user.

    class BreakpointEvent(StopEvent)
     |  GDB breakpoint stop event object
     |
     |  Method resolution order:
     |      BreakpointEvent
     |      StopEvent
     |      ThreadEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class ClearObjFilesEvent(Event)
     |  GDB clear object files event object
     |
     |  Method resolution order:
     |      ClearObjFilesEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Command(builtins.object)
     |  GDB command object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  dont_repeat(...)
     |      Prevent command repetition when user enters empty line.

    class ContinueEvent(ThreadEvent)
     |  GDB continue event object
     |
     |  Method resolution order:
     |      ContinueEvent
     |      ThreadEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Event(builtins.object)
     |  GDB event object
     |
     |  Data descriptors defined here:
     |
     |  __dict__
     |      The __dict__ for this event.

    class EventRegistry(builtins.object)
     |  GDB event registry object
     |
     |  Methods defined here:
     |
     |  connect(...)
     |      Add function
     |
     |  disconnect(...)
     |      Remove function

    class ExitedEvent(Event)
     |  GDB exited event object
     |
     |  Method resolution order:
     |      ExitedEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Field(builtins.object)
     |  GDB field object
     |
     |  Data descriptors defined here:
     |
     |  __dict__
     |      The __dict__ for this field.

    class FinishBreakpoint(Breakpoint)
     |  GDB finish breakpoint object
     |
     |  Method resolution order:
     |      FinishBreakpoint
     |      Breakpoint
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  return_value
     |      gdb.Value object representing the return value, if any. None otherwise.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from Breakpoint:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  delete(...)
     |      Delete the underlying GDB breakpoint.
     |
     |  is_valid(...)
     |      Return true if this breakpoint is valid, false if not.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Breakpoint:
     |
     |  commands
     |      Commands of the breakpoint, as specified by the user.
     |
     |  condition
     |      Condition of the breakpoint, as specified by the user,or None if no condition set.
     |
     |  enabled
     |      Boolean telling whether the breakpoint is enabled.
     |
     |  expression
     |      Expression of the breakpoint, as specified by the user.
     |
     |  hit_count
     |      Number of times the breakpoint has been hit.
     |      Can be set to zero to clear the count. No other value is valid
     |      when setting this property.
     |
     |  ignore_count
     |      Number of times this breakpoint should be automatically continued.
     |
     |  location
     |      Location of the breakpoint, as specified by the user.
     |
     |  number
     |      Breakpoint's number assigned by GDB.
     |
     |  silent
     |      Boolean telling whether the breakpoint is silent.
     |
     |  task
     |      Thread ID for the breakpoint.
     |      If the value is a task ID (integer), then this is an Ada task-specific breakpoint.
     |      If the value is None, then this breakpoint is not task-specific.
     |      No other type of value can be used.
     |
     |  temporary
     |      Whether this breakpoint is a temporary breakpoint.
     |
     |  thread
     |      Thread ID for the breakpoint.
     |      If the value is a thread ID (integer), then this is a thread-specific breakpoint.
     |      If the value is None, then this breakpoint is not thread-specific.
     |      No other type of value can be used.
     |
     |  type
     |      Type of breakpoint.
     |
     |  visible
     |      Whether the breakpoint is visible to the user.

    class Frame(builtins.object)
     |  GDB frame object
     |
     |  Methods defined here:
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  architecture(...)
     |      architecture () -> gdb.Architecture.
     |      Return the architecture of the frame.
     |
     |  block(...)
     |      block () -> gdb.Block.
     |      Return the frame's code block.
     |
     |  find_sal(...)
     |      find_sal () -> gdb.Symtab_and_line.
     |      Return the frame's symtab and line.
     |
     |  function(...)
     |      function () -> gdb.Symbol.
     |      Returns the symbol for the function corresponding to this frame.
     |
     |  thread
     |      Thread ID for the breakpoint.
     |      If the value is a thread ID (integer), then this is a thread-specific breakpoint.
     |      If the value is None, then this breakpoint is not thread-specific.
     |      No other type of value can be used.
     |
     |  type
     |      Type of breakpoint.
     |
     |  visible
     |      Whether the breakpoint is visible to the user.

    class Frame(builtins.object)
     |  GDB frame object
     |
     |  Methods defined here:
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  architecture(...)
     |      architecture () -> gdb.Architecture.
     |      Return the architecture of the frame.
     |
     |  block(...)
     |      block () -> gdb.Block.
     |      Return the frame's code block.
     |
     |  find_sal(...)
     |      find_sal () -> gdb.Symtab_and_line.
     |      Return the frame's symtab and line.
     |
     |  function(...)
     |      function () -> gdb.Symbol.
     |      Returns the symbol for the function corresponding to this frame.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this frame is valid, false if not.
     |
     |  name(...)
     |      name () -> String.
     |      Return the function name of the frame, or None if it can't be determined.
     |
     |  newer(...)
     |      newer () -> gdb.Frame.
     |      Return the frame called by this frame.
     |
     |  older(...)
     |      older () -> gdb.Frame.
     |      Return the frame that called this frame.
     |
     |  pc(...)
     |      pc () -> Long.
     |      Return the frame's resume address.
     |
     |  read_register(...)
     |      read_register (register_name) -> gdb.Value
     |      Return the value of the register in the frame.
     |
     |  read_var(...)
     |      read_var (variable) -> gdb.Value.
     |      Return the value of the variable in this frame.
     |
     |  select(...)
     |      Select this frame as the user's current frame.
     |
     |  type(...)
     |      type () -> Integer.
     |      Return the type of the frame.
     |
     |  unwind_stop_reason(...)
     |      unwind_stop_reason () -> Integer.
     |      Return the reason why it's not possible to find frames older than this.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None

    class Function(builtins.object)
     |  GDB function object
     |
     |  Methods defined here:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

    class GdbError(builtins.Exception)
     |
     |  Method resolution order:
     |      GdbError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      helper for pickle
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class GdbOutputErrorFile(_GdbFile)
     |  Method resolution order:
     |      GdbOutputErrorFile
     |      _GdbFile
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  write(self, s)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _GdbFile:
     |
     |  close(self)
     |
     |  flush(self)
     |
     |  isatty(self)
     |
     |  writelines(self, iterable)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _GdbFile:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _GdbFile:
     |
     |  encoding = 'UTF-8'
     |
     |  errors = 'strict'

    class GdbOutputFile(_GdbFile)
     |  Method resolution order:
     |      GdbOutputFile
     |      _GdbFile
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  write(self, s)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from _GdbFile:
     |
     |  close(self)
     |
     |  flush(self)
     |
     |  isatty(self)
     |
     |  writelines(self, iterable)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _GdbFile:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _GdbFile:
     |
     |  encoding = 'UTF-8'
     |
     |  errors = 'strict'

    class Inferior(builtins.object)
     |  GDB inferior object
     |
     |  Methods defined here:
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this inferior is valid, false if not.
     |
     |  read_memory(...)
     |      read_memory (address, length) -> buffer
     |      Return a buffer object for reading from the inferior's memory.
     |
     |  search_memory(...)
     |      search_memory (address, length, pattern) -> long
     |      Return a long with the address of a match, or None.
     |
     |  threads(...)
     |      Return all the threads of this inferior.
     |
     |  write_memory(...)
     |      write_memory (address, buffer [, length])
     |      Write the given buffer object to the inferior's memory.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  num
     |      ID of inferior, as assigned by GDB.
     |
     |  pid
     |      PID of inferior, as assigned by the OS.
     |
     |  close(self)
     |
     |  flush(self)
     |
     |  isatty(self)
     |
     |  writelines(self, iterable)
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _GdbFile:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from _GdbFile:
     |
     |  encoding = 'UTF-8'
     |
     |  errors = 'strict'

    class Inferior(builtins.object)
     |  GDB inferior object
     |
     |  Methods defined here:
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this inferior is valid, false if not.
     |
     |  read_memory(...)
     |      read_memory (address, length) -> buffer
     |      Return a buffer object for reading from the inferior's memory.
     |
     |  search_memory(...)
     |      search_memory (address, length, pattern) -> long
     |      Return a long with the address of a match, or None.
     |
     |  threads(...)
     |      Return all the threads of this inferior.
     |
     |  write_memory(...)
     |      write_memory (address, buffer [, length])
     |      Write the given buffer object to the inferior's memory.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  num
     |      ID of inferior, as assigned by GDB.
     |
     |  pid
     |      PID of inferior, as assigned by the OS.
     |
     |  was_attached
     |      True if the inferior was created using 'attach'.

    class InferiorCallPostEvent(Event)
     |  GDB inferior function post-call event object
     |
     |  Method resolution order:
     |      InferiorCallPostEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class InferiorCallPreEvent(Event)
     |  GDB inferior function pre-call event object
     |
     |  Method resolution order:
     |      InferiorCallPreEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class InferiorThread(builtins.object)
     |  GDB thread object
     |
     |  Methods defined here:
     |
     |  is_exited(...)
     |      is_exited () -> Boolean
     |      Return whether the thread is exited.
     |
     |  is_running(...)
     |      is_running () -> Boolean
     |      Return whether the thread is running.
     |
     |  is_stopped(...)
     |      is_stopped () -> Boolean
     |      Return whether the thread is stopped.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this inferior thread is valid, false if not.
     |
     |  switch(...)
     |      switch ()
     |      Makes this the GDB selected thread.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  global_num
     |      Global number of the thread, as assigned by GDB.
     |
     |  inferior
     |      The Inferior object this thread belongs to.
     |
     |  name
     |      The name of the thread, as set by the user or the OS.
     |
     |  num
     |      Per-inferior number of the thread, as assigned by GDB.
     |
     |  ptid
     |      ID of the thread, as assigned by the OS.

    class LineTable(builtins.object)
     |  GDB line table object
     |
     |  Methods defined here:
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  has_line(...)
     |      has_line (lineno) -> Boolean
     |      Return TRUE if this line has executable information, FALSE if not.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return True if this LineTable is valid, False if not.
     |
     |  line(...)
     |      line (lineno) -> Tuple
     |      Return executable locations for a given source line.
     |
     |  source_lines(...)
     |      source_lines () -> List
     |      Return a list of all executable source lines.

    class LineTableEntry(builtins.object)
     |  GDB line table entry object
     |
     |  Data descriptors defined here:
     |
     |  line
     |      The line number in the source file.
     |
     |  pc
     |      The memory address for this line number.

    class LineTableIterator(builtins.object)
     |  GDB line table iterator object
     |
     |  Methods defined here:
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __next__(self, /)
     |      Implement next(self).
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return True if this LineTable iterator is valid, False if not.

    class Membuf(builtins.object)
     |  GDB memory buffer object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __str__(self, /)
     |      Return str(self).

    class MemoryChangedEvent(Event)
     |  GDB memory change event object
     |
     |  Method resolution order:
     |      MemoryChangedEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class MemoryError(error)
     |  Unspecified run-time error.
     |
     |  Method resolution order:
     |      MemoryError
     |      error
     |      builtins.RuntimeError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors inherited from error:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.RuntimeError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      helper for pickle
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

    class NewObjFileEvent(Event)
     |  GDB new object file event object
     |
     |  Method resolution order:
     |      NewObjFileEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Objfile(builtins.object)
     |  GDB objfile object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  add_separate_debug_file(...)
     |      add_separate_debug_file (file_name).
     |      Add FILE_NAME to the list of files containing debug info for the objfile.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this object file is valid, false if not.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      The __dict__ for this objfile.
     |
     |  build_id
     |      The objfile's build id, or None.
     |
     |  filename
     |      The objfile's filename, or None.
     |
     |  frame_filters
     |      Frame Filters.
     |
     |  frame_unwinders
     |      Frame Unwinders
     |
     |  owner
     |      The objfile owner of separate debug info objfiles, or None.
     |
     |  pretty_printers
     |      Pretty printers.
     |
     |  progspace
     |      The objfile's progspace, or None.
     |
     |  type_printers
     |      Type printers.
     |
     |  username
     |      The name of the objfile as provided by the user, or None.
     |
     |  xmethods
     |      Debug methods.

    class Parameter(builtins.object)
     |  GDB parameter object
     |
     |  Methods defined here:

    class Objfile(builtins.object)
     |  GDB objfile object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  add_separate_debug_file(...)
     |      add_separate_debug_file (file_name).
     |      Add FILE_NAME to the list of files containing debug info for the objfile.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this object file is valid, false if not.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      The __dict__ for this objfile.
     |
     |  build_id
     |      The objfile's build id, or None.
     |
     |  filename
     |      The objfile's filename, or None.
     |
     |  frame_filters
     |      Frame Filters.
     |
     |  frame_unwinders
     |      Frame Unwinders
     |
     |  owner
     |      The objfile owner of separate debug info objfiles, or None.
     |
     |  pretty_printers
     |      Pretty printers.
     |
     |  progspace
     |      The objfile's progspace, or None.
     |
     |  type_printers
     |      Type printers.
     |
     |  username
     |      The name of the objfile as provided by the user, or None.
     |
     |  xmethods
     |      Debug methods.

    class Parameter(builtins.object)
     |  GDB parameter object
     |
     |  Methods defined here:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).

    class PendingFrame(builtins.object)
     |  GDB PendingFrame object
     |
     |  Methods defined here:
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  create_unwind_info(...)
     |      create_unwind_info (FRAME_ID) -> gdb.UnwindInfo
     |      Construct UnwindInfo for this PendingFrame, using FRAME_ID
     |      to identify it.
     |
     |  read_register(...)
     |      read_register (REG) -> gdb.Value
     |      Return the value of the REG in the frame.

    class Progspace(builtins.object)
     |  GDB progspace object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      The __dict__ for this progspace.
     |
     |  filename
     |      The progspace's main filename, or None.
     |
     |  frame_filters
     |      Frame filters.
     |
     |  frame_unwinders
     |      Frame unwinders.
     |
     |  pretty_printers
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).

    class PendingFrame(builtins.object)
     |  GDB PendingFrame object
     |
     |  Methods defined here:
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  create_unwind_info(...)
     |      create_unwind_info (FRAME_ID) -> gdb.UnwindInfo
     |      Construct UnwindInfo for this PendingFrame, using FRAME_ID
     |      to identify it.
     |
     |  read_register(...)
     |      read_register (REG) -> gdb.Value
     |      Return the value of the REG in the frame.

    class Progspace(builtins.object)
     |  GDB progspace object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      The __dict__ for this progspace.
     |
     |  filename
     |      The progspace's main filename, or None.
     |
     |  frame_filters
     |      Frame filters.
     |
     |  frame_unwinders
     |      Frame unwinders.
     |
     |  pretty_printers
     |      Pretty printers.
     |
     |  type_printers
     |      Type printers.
     |
     |  xmethods
     |      Debug methods.

    class RegisterChangedEvent(Event)
     |  GDB register change event object
     |
     |  Method resolution order:
     |      RegisterChangedEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class SignalEvent(StopEvent)
     |  GDB signal event object
     |
     |  Method resolution order:
     |      SignalEvent
     |      StopEvent
     |      ThreadEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class StopEvent(ThreadEvent)
     |  GDB stop event object
     |
     |  Method resolution order:
     |      StopEvent
     |      ThreadEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Symbol(builtins.object)
     |  GDB symbol object
     |
     |  Methods defined here:
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this symbol is valid, false if not.
     |
     |  value(...)
     |      value ([frame]) -> gdb.Value
     |      Return the value of the symbol.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  addr_class
     |      Address class of the symbol.
     |
     |  is_argument
     |      True if the symbol is an argument of a function.
     |
     |  is_constant
     |      True if the symbol is a constant.
     |
     |  is_function
     |      True if the symbol is a function or method.
     |
     |  is_variable
     |      True if the symbol is a variable.
     |
     |  line
     |      The source line number at which the symbol was defined.
     |
     |  linkage_name
     |      Name of the symbol, as used by the linker (i.e., may be mangled).
     |
     |  name
     |      Name of the symbol, as it appears in the source code.
     |
     |  needs_frame
     |      True if the symbol requires a frame for evaluation.
     |
     |  print_name
     |      Name of the symbol in a form suitable for output.
     |      This is either name or linkage_name, depending on whether the user asked GDB
     |      to display demangled or mangled names.
     |
     |  symtab
     |      Symbol table in which the symbol appears.
     |
     |  type
     |      Type of the symbol.

    class Symtab(builtins.object)
     |  GDB symtab object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  fullname(...)
     |      fullname () -> String.
     |      Return the symtab's full source filename.
     |
     |  global_block(...)
     |      global_block () -> gdb.Block.
     |      Return the global block of the symbol table.
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this symbol table is valid, false if not.
     |
     |  linetable(...)
     |      linetable () -> gdb.LineTable.
     |      Return the LineTable associated with this symbol table
     |
     |  static_block(...)
     |      static_block () -> gdb.Block.
     |      Return the static block of the symbol table.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  filename
     |      The symbol table's source filename.
     |
     |  objfile
     |      The symtab's objfile.
     |
     |  producer
     |      The name/version of the program that compiled this symtab.

    class Symtab_and_line(builtins.object)
     |  GDB symtab_and_line object
     |
     |  Methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  is_valid(...)
     |      is_valid () -> Boolean.
     |      Return true if this symbol table and line is valid, false if not.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  last
     |      Return the symtab_and_line's last address.
     |
     |  line
     |      Return the symtab_and_line's line.
     |
     |  pc
     |      Return the symtab_and_line's pc.
     |
     |  symtab
     |      Symtab object.

    class ThreadEvent(Event)
     |  GDB thread event object
     |
     |  Method resolution order:
     |      ThreadEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Type(builtins.object)
     |  GDB type object
     |
     |  Methods defined here:
     |
     |  __bool__(self, /)
     |      self != 0
     |
     |  __contains__(...)
     |      T.__contains__(k) -> True if T has a field named k, else False
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  line
     |      Return the symtab_and_line's line.
     |
     |  pc
     |      Return the symtab_and_line's pc.
     |
     |  symtab
     |      Symtab object.

    class ThreadEvent(Event)
     |  GDB thread event object
     |
     |  Method resolution order:
     |      ThreadEvent
     |      Event
     |      builtins.object
     |
     |  Data descriptors inherited from Event:
     |
     |  __dict__
     |      The __dict__ for this event.

    class Type(builtins.object)
     |  GDB type object
     |
     |  Methods defined here:
     |
     |  __bool__(self, /)
     |      self != 0
     |
     |  __contains__(...)
     |      T.__contains__(k) -> True if T has a field named k, else False
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  array(...)
     |      array ([LOW_BOUND,] HIGH_BOUND) -> Type
     |      Return a type which represents an array of objects of this type.
     |      The bounds of the array are [LOW_BOUND, HIGH_BOUND] inclusive.
     |      If LOW_BOUND is omitted, a value of zero is used.
     |
     |  const(...)
     |      const () -> Type
     |      Return a const variant of this type.
     |
     |  fields(...)
     |      fields () -> list
     |      Return a list holding all the fields of this type.
     |      Each field is a gdb.Field object.
     |
     |  get(...)
     |      T.get(k[,default]) -> returns field named k in T, if it exists;
     |      otherwise returns default, if supplied, or None if not.
     |
     |  has_key(...)
     |      T.has_key(k) -> True if T has a field named k, else False
     |
     |  items(...)
     |      items () -> list
     |      Return a list of (name, field) pairs of this type.
     |      Each field is a gdb.Field object.
     |
     |  iteritems(...)
     |      iteritems () -> an iterator over the (name, field)
     |      pairs of this type.  Each field is a gdb.Field object.
     |
     |  iterkeys(...)
     |      iterkeys () -> an iterator over the field names of this type.
     |
     |  itervalues(...)
     |      itervalues () -> an iterator over the fields of this type.
     |      Each field is a gdb.Field object.
     |
     |  keys(...)
     |      keys () -> list
     |      Return a list holding all the fields names of this type.
     |
     |  optimized_out(...)
     |      optimized_out() -> Value
     |      Return optimized out value of this type.
     |
     |  pointer(...)
     |      pointer () -> Type
     |      Return a type of pointer to this type.
     |
     |  range(...)
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  array(...)
     |      array ([LOW_BOUND,] HIGH_BOUND) -> Type
     |      Return a type which represents an array of objects of this type.
     |      The bounds of the array are [LOW_BOUND, HIGH_BOUND] inclusive.
     |      If LOW_BOUND is omitted, a value of zero is used.
     |
     |  const(...)
     |      const () -> Type
     |      Return a const variant of this type.
     |
     |  fields(...)
     |      fields () -> list
     |      Return a list holding all the fields of this type.
     |      Each field is a gdb.Field object.
     |
     |  get(...)
     |      T.get(k[,default]) -> returns field named k in T, if it exists;
     |      otherwise returns default, if supplied, or None if not.
     |
     |  has_key(...)
     |      T.has_key(k) -> True if T has a field named k, else False
     |
     |  items(...)
     |      items () -> list
     |      Return a list of (name, field) pairs of this type.
     |      Each field is a gdb.Field object.
     |
     |  iteritems(...)
     |      iteritems () -> an iterator over the (name, field)
     |      pairs of this type.  Each field is a gdb.Field object.
     |
     |  iterkeys(...)
     |      iterkeys () -> an iterator over the field names of this type.
     |
     |  itervalues(...)
     |      itervalues () -> an iterator over the fields of this type.
     |      Each field is a gdb.Field object.
     |
     |  keys(...)
     |      keys () -> list
     |      Return a list holding all the fields names of this type.
     |
     |  optimized_out(...)
     |      optimized_out() -> Value
     |      Return optimized out value of this type.
     |
     |  pointer(...)
     |      pointer () -> Type
     |      Return a type of pointer to this type.
     |
     |  range(...)
     |      range () -> tuple
     |      Return a tuple containing the lower and upper range for this type.
     |
     |  reference(...)
     |      reference () -> Type
     |      Return a type of reference to this type.
     |
     |  strip_typedefs(...)
     |      strip_typedefs () -> Type
     |      Return a type formed by stripping this type of all typedefs.
     |
     |  target(...)
     |      target () -> Type
     |      Return the target type of this type.
     |
     |  template_argument(...)
     |      template_argument (arg, [block]) -> Type
     |      Return the type of a template argument.
     |
     |  unqualified(...)
     |      unqualified () -> Type
     |      Return a variant of this type without const or volatile attributes.
     |
     |  values(...)
     |      values () -> list
     |      Return a list holding all the fields of this type.
     |      Each field is a gdb.Field object.
     |
     |  vector(...)
     |      vector ([LOW_BOUND,] HIGH_BOUND) -> Type
     |      Return a type which represents a vector of objects of this type.
     |      The bounds of the array are [LOW_BOUND, HIGH_BOUND] inclusive.
     |      If LOW_BOUND is omitted, a value of zero is used.
     |      Vectors differ from arrays in that if the current language has C-style
     |      arrays, vectors don't decay to a pointer to the first element.
     |      They are first class values.
     |
     |  volatile(...)
     |      volatile () -> Type
     |      Return a volatile variant of this type
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  code
     |      The code for this type.
     |
     |  name
     |      The name for this type, or None.
     |
     |  sizeof
     |      The size of this type, in bytes.
     |
     |  tag
     |      The tag name for this type, or None.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __hash__ = None

    class TypeIterator(builtins.object)
     |  GDB type iterator object
     |
     |  Methods defined here:
     |
     |  __iter__(self, /)
     |      Implement iter(self).
     |
     |  __next__(self, /)
     |      Implement next(self).

    class UnwindInfo(builtins.object)
     |  GDB UnwindInfo object
     |
     |  Methods defined here:
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  add_saved_register(...)
     |      add_saved_register (REG, VALUE) -> None
     |      Set the value of the REG in the previous frame to VALUE.

    class Value(builtins.object)
     |  GDB value object
     |
     |  Methods defined here:
     |
     |  __abs__(self, /)
     |      abs(self)
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __and__(self, value, /)
     |      Return self&value.
     |
     |  __bool__(self, /)
     |      self != 0
     |
     |  __call__(self, /, *args, **kwargs)
     |      Call self as a function.
     |
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __float__(self, /)
     |      float(self)
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getitem__(self, key, /)
     |      Return self[key].
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __int__(self, /)
     |      int(self)
     |
     |  __invert__(self, /)
     |      ~self
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __len__(self, /)
     |      Return len(self).
     |
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mod__(self, value, /)
     |      Return self%value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __neg__(self, /)
     |      -self
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  __or__(self, value, /)
     |      Return self|value.
     |
     |  __pos__(self, /)
     |      +self
     |
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __rand__(self, value, /)
     |      Return value&self.
     |
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __ror__(self, value, /)
     |      Return value|self.
     |
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |
     |  __rxor__(self, value, /)
     |      Return value^self.
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  __truediv__(self, value, /)
     |      Return self/value.
     |
     |  __xor__(self, value, /)
     |      Return self^value.
     |
     |  cast(...)
     |      Cast the value to the supplied type.
     |
     |  const_value(...)
     |      Return a 'const' qualied version of the same value.
     |
     |  dereference(...)
     |      Dereferences the value.
     |
     |  dynamic_cast(...)
     |      Return value&self.
     |
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __ror__(self, value, /)
     |      Return value|self.
     |
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |
     |  __rxor__(self, value, /)
     |      Return value^self.
     |
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  __truediv__(self, value, /)
     |      Return self/value.
     |
     |  __xor__(self, value, /)
     |      Return self^value.
     |
     |  cast(...)
     |      Cast the value to the supplied type.
     |
     |  const_value(...)
     |      Return a 'const' qualied version of the same value.
     |
     |  dereference(...)
     |      Dereferences the value.
     |
     |  dynamic_cast(...)
     |      dynamic_cast (gdb.Type) -> gdb.Value
     |      Cast the value to the supplied type, as if by the C++ dynamic_cast operator.
     |
     |  fetch_lazy(...)
     |      Fetches the value from the inferior, if it was lazy.
     |
     |  lazy_string(...)
     |      lazy_string ([encoding]  [, length]) -> lazy_string
     |      Return a lazy string representation of the value.
     |
     |  reference_value(...)
     |      Return a value of type TYPE_CODE_REF referencing this value.
     |
     |  referenced_value(...)
     |      Return the value referenced by a TYPE_CODE_REF or TYPE_CODE_PTR value.
     |
     |  reinterpret_cast(...)
     |      reinterpret_cast (gdb.Type) -> gdb.Value
     |      Cast the value to the supplied type, as if by the C++
     |      reinterpret_cast operator.
     |
     |  string(...)
     |      string ([encoding] [, errors] [, length]) -> string
     |      Return Unicode string representation of the value.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  address
     |      The address of the value.
     |
     |  dynamic_type
     |      Dynamic type of the value.
     |
     |  is_lazy
     |      Boolean telling whether the value is lazy (not fetched yet
     |      from the inferior).  A lazy value is fetched when needed, or when
     |      the "fetch_lazy()" method is called.
     |
     |  is_optimized_out
     |      Boolean telling whether the value is optimized out (i.e., not available).
     |
     |  type
     |      Type of the value.

    class error(builtins.RuntimeError)
     |  Unspecified run-time error.
     |
     |  Method resolution order:
     |      error
     |      builtins.RuntimeError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |      dynamic_cast (gdb.Type) -> gdb.Value
     |      Cast the value to the supplied type, as if by the C++ dynamic_cast operator.
     |
     |  fetch_lazy(...)
     |      Fetches the value from the inferior, if it was lazy.
     |
     |  lazy_string(...)
     |      lazy_string ([encoding]  [, length]) -> lazy_string
     |      Return a lazy string representation of the value.
     |
     |  reference_value(...)
     |      Return a value of type TYPE_CODE_REF referencing this value.
     |
     |  referenced_value(...)
     |      Return the value referenced by a TYPE_CODE_REF or TYPE_CODE_PTR value.
     |
     |  reinterpret_cast(...)
     |      reinterpret_cast (gdb.Type) -> gdb.Value
     |      Cast the value to the supplied type, as if by the C++
     |      reinterpret_cast operator.
     |
     |  string(...)
     |      string ([encoding] [, errors] [, length]) -> string
     |      Return Unicode string representation of the value.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  address
     |      The address of the value.
     |
     |  dynamic_type
     |      Dynamic type of the value.
     |
     |  is_lazy
     |      Boolean telling whether the value is lazy (not fetched yet
     |      from the inferior).  A lazy value is fetched when needed, or when
     |      the "fetch_lazy()" method is called.
     |
     |  is_optimized_out
     |      Boolean telling whether the value is optimized out (i.e., not available).
     |
     |  type
     |      Type of the value.

    class error(builtins.RuntimeError)
     |  Unspecified run-time error.
     |
     |  Method resolution order:
     |      error
     |      builtins.RuntimeError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |
     |  Data descriptors defined here:
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.RuntimeError:
     |
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      helper for pickle
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |
     |  __setstate__(...)
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |
     |  __cause__
     |      exception cause
     |
     |  __context__
     |      exception context
     |
     |  __dict__
     |
     |  __suppress_context__
     |
     |  __traceback__
     |
     |  args

FUNCTIONS
    GdbSetPythonDirectory(dir)
        Update sys.path, reload gdb and auto-load packages.

    auto_load_packages()

    block_for_pc(...)
        Return the block containing the given pc value, or None.

    breakpoints(...)
        Return a tuple of all breakpoint objects

    current_objfile(...)
        Return the current Objfile being loaded, or None.

    current_progspace(...)
        Return the current Progspace.

    decode_line(...)
        decode_line (String) -> Tuple.  Decode a string argument the way
        that 'break' or 'edit' does.  Return a tuple containing two elements.
        The first element contains any unparsed portion of the String parameter
        (or None if the string was fully parsed).  The second element contains
        a tuple that contains all the locations that match, represented as
        gdb.Symtab_and_line objects (or None).

    default_visualizer(...)
        Find the default visualizer for a Value.

    execute(...)
        execute (command [, from_tty] [, to_string]) -> [String]
        Evaluate command, a string, as a gdb CLI command.  Optionally returns
        a Python String containing the output of the command if to_string is
        set to True.

    execute_unwinders(pending_frame)
        Internal function called from GDB to execute all unwinders.

        Runs each currently enabled unwinder until it finds the one that
        can unwind given frame.

        Arguments:
            pending_frame: gdb.PendingFrame instance.
        Returns:
            gdb.UnwindInfo instance or None.

    find_pc_line(...)
        find_pc_line (pc) -> Symtab_and_line.
        Return the gdb.Symtab_and_line object corresponding to the pc value.

    flush(...)
        Flush gdb's filtered stdout stream.

    frame_stop_reason_string(...)
        stop_reason_string (Integer) -> String.
        Return a string explaining unwind stop reason.

    history(...)
        Get a value from history

    inferiors(...)
        inferiors () -> (gdb.Inferior, ...).
        Return a tuple containing all inferiors.

    lookup_global_symbol(...)
        lookup_global_symbol (name [, domain]) -> symbol
        Return the symbol corresponding to the given name (or None).

    lookup_objfile(...)
        lookup_objfile (name, [by_build_id]) -> objfile
        Look up the specified objfile.
        If by_build_id is True, the objfile is looked up by using name
        as its build id.

    lookup_symbol(...)
        lookup_symbol (name [, block] [, domain]) -> (symbol, is_field_of_this)
        Return a tuple with the symbol corresponding to the given name (or None) and
        a boolean indicating if name is a field of the current implied argument
        `this' (when the current language is object-oriented).

    lookup_type(...)
        lookup_type (name [, block]) -> type
        Return a Type corresponding to the given name.

    newest_frame(...)
        newest_frame () -> gdb.Frame.
        Return the newest frame object.

    objfiles(...)
        Return a sequence of all loaded objfiles.

    parameter(...)
        Return a gdb parameter's value

    parse_and_eval(...)
        parse_and_eval (String) -> Value.
        Parse String as an expression, evaluate it, and return the result as a Value.

    post_event(...)
        Post an event into gdb's event loop.

    progspaces(...)
        Return a sequence of all progspaces.

    selected_frame(...)
        selected_frame () -> gdb.Frame.
        Return the selected frame object.

    selected_inferior(...)
        selected_inferior () -> gdb.Inferior.
        Return the selected inferior object.

    selected_thread(...)
        selected_thread () -> gdb.InferiorThread.
        Return the selected thread object.

    solib_name(...)
        solib_name (Long) -> String.
        Return the name of the shared library holding a given address, or None.

    string_to_argv(...)
        string_to_argv (String) -> Array.
        Parse String and return an argv-like array.
        Arguments are separate by spaces and may be quoted.

    target_charset(...)
        target_charset () -> string.
        Return the name of the current target charset.

    target_wide_charset(...)
        target_wide_charset () -> string.
        Return the name of the current target wide charset.

    write(...)
        Write a string using gdb's filtered stream.

DATA
    ARCH_FRAME = 5
    BP_ACCESS_WATCHPOINT = 9
    BP_BREAKPOINT = 1
    BP_HARDWARE_WATCHPOINT = 7
    BP_NONE = 0
    BP_READ_WATCHPOINT = 8
    BP_WATCHPOINT = 6
    COMMAND_BREAKPOINTS = 6
    COMMAND_DATA = 1
    COMMAND_FILES = 3
    COMMAND_MAINTENANCE = 11
    COMMAND_NONE = -1
    COMMAND_OBSCURE = 10
    COMMAND_RUNNING = 0
    COMMAND_STACK = 2
    COMMAND_STATUS = 5
    COMMAND_SUPPORT = 4
    COMMAND_TRACEPOINTS = 7
    COMMAND_USER = 14
    COMPLETE_COMMAND = 3
    COMPLETE_EXPRESSION = 5
    COMPLETE_FILENAME = 1
    COMPLETE_LOCATION = 2
    COMPLETE_NONE = 0
    COMPLETE_SYMBOL = 4
    DUMMY_FRAME = 1
    FRAME_UNWIND_INNER_ID = 4
    FRAME_UNWIND_MEMORY_ERROR = 7
    FRAME_UNWIND_NO_REASON = 0
    FRAME_UNWIND_NO_SAVED_PC = 6
    FRAME_UNWIND_NULL_ID = 1
    FRAME_UNWIND_OUTERMOST = 2
    FRAME_UNWIND_SAME_ID = 5
    FRAME_UNWIND_UNAVAILABLE = 3
    HOST_CONFIG = 'x86_64-linux-gnu'
    INLINE_FRAME = 2
    NORMAL_FRAME = 0
    PARAM_AUTO_BOOLEAN = 1
    PARAM_BOOLEAN = 0
    PARAM_ENUM = 11
    PARAM_FILENAME = 7
    PARAM_INTEGER = 3
    PARAM_OPTIONAL_FILENAME = 6
    PARAM_STRING = 4
    PARAM_STRING_NOESCAPE = 5
    PARAM_UINTEGER = 2
    PARAM_ZINTEGER = 8
    PYTHONDIR = '/usr/share/gdb/python'
    SENTINEL_FRAME = 6
    SIGTRAMP_FRAME = 4
    STDERR = 1
    STDLOG = 2
    STDOUT = 0
    SYMBOL_FUNCTIONS_DOMAIN = 1
    SYMBOL_LABEL_DOMAIN = 4
    SYMBOL_LOC_ARG = 4
    SYMBOL_LOC_BLOCK = 10
    SYMBOL_LOC_COMPUTED = 14
    SYMBOL_LOC_CONST = 1
    SYMBOL_LOC_CONST_BYTES = 11
    SYMBOL_LOC_LABEL = 9
    SYMBOL_LOC_LOCAL = 7
    SYMBOL_LOC_OPTIMIZED_OUT = 13
    SYMBOL_LOC_REF_ARG = 5
    SYMBOL_LOC_REGISTER = 3
    SYMBOL_LOC_REGPARM_ADDR = 6
    SYMBOL_LOC_STATIC = 2
    SYMBOL_LOC_TYPEDEF = 8
    SYMBOL_LOC_UNDEF = 0
    SYMBOL_LOC_UNRESOLVED = 12
    SYMBOL_STRUCT_DOMAIN = 2
    SYMBOL_TYPES_DOMAIN = 2
    SYMBOL_UNDEF_DOMAIN = 0
    SYMBOL_VARIABLES_DOMAIN = 0
    SYMBOL_VAR_DOMAIN = 1
    TAILCALL_FRAME = 3
    TARGET_CONFIG = 'x86_64-linux-gnu'
    TYPE_CODE_ARRAY = 2
    TYPE_CODE_BITSTRING = -1
    TYPE_CODE_BOOL = 20
    TYPE_CODE_CHAR = 19
    TYPE_CODE_COMPLEX = 21
    TYPE_CODE_DECFLOAT = 24
    TYPE_CODE_ENUM = 5
    TYPE_CODE_ERROR = 14
    TYPE_CODE_FLAGS = 6
    TYPE_CODE_FLT = 9
    TYPE_CODE_FUNC = 7
    TYPE_CODE_INT = 8
    TYPE_CODE_INTERNAL_FUNCTION = 26
    TYPE_CODE_MEMBERPTR = 17
    TYPE_CODE_METHOD = 15
    SYMBOL_LOC_REGISTER = 3
    SYMBOL_LOC_REGPARM_ADDR = 6
    SYMBOL_LOC_STATIC = 2
    SYMBOL_LOC_TYPEDEF = 8
    SYMBOL_LOC_UNDEF = 0
    SYMBOL_LOC_UNRESOLVED = 12
    SYMBOL_STRUCT_DOMAIN = 2
    SYMBOL_TYPES_DOMAIN = 2
    SYMBOL_UNDEF_DOMAIN = 0
    SYMBOL_VARIABLES_DOMAIN = 0
    SYMBOL_VAR_DOMAIN = 1
    TAILCALL_FRAME = 3
    TARGET_CONFIG = 'x86_64-linux-gnu'
    TYPE_CODE_ARRAY = 2
    TYPE_CODE_BITSTRING = -1
    TYPE_CODE_BOOL = 20
    TYPE_CODE_CHAR = 19
    TYPE_CODE_COMPLEX = 21
    TYPE_CODE_DECFLOAT = 24
    TYPE_CODE_ENUM = 5
    TYPE_CODE_ERROR = 14
    TYPE_CODE_FLAGS = 6
    TYPE_CODE_FLT = 9
    TYPE_CODE_FUNC = 7
    TYPE_CODE_INT = 8
    TYPE_CODE_INTERNAL_FUNCTION = 26
    TYPE_CODE_MEMBERPTR = 17
    TYPE_CODE_METHOD = 15
    TYPE_CODE_METHODPTR = 16
    TYPE_CODE_NAMESPACE = 23
    TYPE_CODE_PTR = 1
    TYPE_CODE_RANGE = 12
    TYPE_CODE_REF = 18
    TYPE_CODE_SET = 11
    TYPE_CODE_STRING = 13
    TYPE_CODE_STRUCT = 3
    TYPE_CODE_TYPEDEF = 22
    TYPE_CODE_UNION = 4
    TYPE_CODE_VOID = 10
    VERSION = '7.11.1'
    WP_ACCESS = 2
    WP_READ = 1
    WP_WRITE = 0
    __warningregistry__ = {'version': 0, ("the imp module is deprecated in...
    frame_filters = {}
    frame_unwinders = []
    packages = ['function', 'command', 'printer']
    pretty_printers = [<gdb.printing.RegexpCollectionPrettyPrinter object>...
    prompt_hook = None
    type_printers = []
    xmethods = []

FILE
    /usr/share/gdb/python/gdb/__init__.py
