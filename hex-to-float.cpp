#include <cstdlib>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::string command = "bash hex-to-float.sh ";
    command.append(argv[1]);
    command.append(" ");
    command.append(argv[2]);
    std::string result = "";
    char buffer[128];
    float result_num;

    // execute bash command
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Error: popen() failed!" << std::endl;
        return 1;
    }
    while (fgets(buffer, 128, pipe) != NULL) {
        result += buffer;
    }
    result_num = std::stof(result);

    pclose(pipe);
    std::cout << "The result is: " << result_num << std::endl;
    return 0;
}

