(.venv) root@localhost:~/gem5/lab/bench# cat memwalk.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

int main(int argc, char** argv){
    // args: <bytes> <stride_bytes> <passes>
    size_t bytes = (argc > 1 ? strtoull(argv[1],0,0) : (64*1024*1024));
    size_t stride = (argc > 2 ? strtoull(argv[2],0,0) : 64);
    int passes = (argc > 3 ? atoi(argv[3]) : 50);

    uint8_t *a;
    if (posix_memalign((void**)&a, 4096, bytes)) { perror("alloc"); return 1; }
    volatile uint64_t sum = 0;

    for (int p=0; p<passes; ++p){
        for (size_t i=0; i<bytes; i+=stride){
            sum += a[i];
            a[i] = (uint8_t)sum;
        }
    }
    fprintf(stderr, "sum=%llu\n", (unsigned long long)sum);
    return 0;
}
