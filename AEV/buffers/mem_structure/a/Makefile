SOURCES=$(wildcard *.c)
OBJS=$(SOURCES:.c=)
ASMS=$(SOURCES:.c=.asm)

# All protections disabled
CFLAGS=-O0 -g -fno-stack-protector -z execstack -no-pie
ASMFLAGS=-S -O0 -fno-stack-protector -no-pie

all: ${OBJS} ${ASMS}

$(OBJS):
	gcc -S ${ASMFLAGS} -o $@.asm $@.c

$(ASMS):
	gcc -S ${ASMFLAGS} -o $@.asm $@.c


clean:
	rm -f ${OBJS} ${ASMS}
