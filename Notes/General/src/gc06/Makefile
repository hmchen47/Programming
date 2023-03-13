# This is a comment line
CC = g++
# CFLAGS will be the option passed to the compiler.
CFLAGS = -c -Wall
OBJECTS = main.o hello.o factial.o

all: prog

prog: $(OBJECTS)
	$(CC) $(OBJECTS) -o prog

%.o: %.cpp
	$(CC) $(CFLAGS) $<


clean:
	rm -f *.o



