
CFLAGS=-O0 -g -fno-stack-protector -z execstack -no-pie


program_flow: 
	gcc ${CFLAGS} -o program_flow program_flow.c

return_to_libc: 
	gcc ${CFLAGS} -o return_to_libc return_to_libc.c

all: program_flow return_to_libc

clean:
	rm -f program_flow
	rm -f return_to_libc
