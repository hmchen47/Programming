CFLAGS += -Wall -Werror -g -O2
SRC     = $(wildcard *.c)
OBJ     = $(SRC:.c=.o)
EXE     = $(subst .c,,$(SRC))

ifdef DEBUG
CFLAGS += -DDEBUG
endif

.PHONY: all clean

all: $(OBJ) $(EXE)

clean:
	rm -rf $(OBJ) $(EXE)

