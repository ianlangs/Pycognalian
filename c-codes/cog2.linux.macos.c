#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int returncode;
    char* stdout_output;
} SubprocessResult;

SubprocessResult subprocess_run(const char* command) {
    SubprocessResult result;
    result.returncode = -1;
    result.stdout_output = NULL;

    FILE* pipe = popen(command, "r");
    if (!pipe) {
        perror("popen");
        return result;
    }

    char buffer[128];
    size_t size = 0;
    char* output = NULL;

    while (fgets(buffer, sizeof(buffer), pipe)) {
        printf("%s", buffer);  // salida en tiempo real

        size_t len = strlen(buffer);
        char* tmp = realloc(output, size + len + 1);
        if (!tmp) {
            free(output);
            output = NULL;
            break;
        }
        output = tmp;
        memcpy(output + size, buffer, len);
        size += len;
        output[size] = '\0';
    }

    int ret = pclose(pipe);
    result.returncode = WEXITSTATUS(ret); // obtenemos el exit code
    result.stdout_output = output;
    return result;
}

char* join(char** strings, int count, const char* sep) {
    if (count == 0) return strdup("");

    size_t sep_len = strlen(sep);
    size_t total_len = 0;

    for (int i = 0; i < count; i++) {
        total_len += strlen(strings[i]);
        if (i < count - 1) total_len += sep_len;
    }

    char* result = malloc(total_len + 1);
    if (!result) return NULL;

    result[0] = '\0';
    for (int i = 0; i < count; i++) {
        strcat(result, strings[i]);
        if (i < count - 1) strcat(result, sep);
    }

    return result;
}

int main(int argc, char *argv[]) {
    char cmd[1024];

    if (argc >= 2) {
        cmd[0] = '\0';
        strcat(cmd, "python3 cog2.py"); // en Linux/macOS es mejor usar python3

        for (int i = 1; i < argc; i++) {
            strcat(cmd, " ");
            strcat(cmd, argv[i]);
        }

        SubprocessResult res = subprocess_run(cmd);
        free(res.stdout_output);

    } else {
        SubprocessResult res = subprocess_run("python3 cog2.py a a a a a a a a a");
        free(res.stdout_output);
    }

    return 0;
}