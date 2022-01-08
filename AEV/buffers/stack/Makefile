SOURCES=$(wildcard *.c)
OBJS=$(SOURCES:.c=)
ASMS=$(SOURCES:.c=.asm)

# All protections disabled
CFLAGS=-O0 -g -fno-stack-protector -z execstack -no-pie
ASMFLAGS=-S -O0 -fno-stack-protector -no-pie  -fno-asynchronous-unwind-tables -fno-exceptions -fverbose-asm -masm=intel

all: ${OBJS}

$(OBJS):
	gcc ${CFLAGS} -o $@ $@.c
	gcc ${ASMFLAGS} -o $@.asm $@.c


clean:
	rm -f ${OBJS} ${ASMS}
