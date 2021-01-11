import os, re, functools, platform

projDir = os.getcwd()
conanfileDir = os.path.join(projDir, "src1")
buildDir = os.path.join(projDir, "out", "build")


def conan_install(target_dir, args):
    os.chdir(target_dir)
    os.system("conan install " + conanfileDir + args)
    os.chdir(projDir)


def targets_setup(targets, args):
    for target in targets:
        target_dir = os.path.join(buildDir, target)
        if os.path.exists(target_dir):
            build_type = re.search("\w+$", target).group(0)
            argsCopy = args.copy()
            argsCopy[0] += build_type
            argsString = functools.reduce(lambda p, n: p + n, argsCopy)
            conan_install(target_dir, argsString)


if platform.system() == "Windows":
    win_targets = ["x64-Debug", "x64-Release"]
    args = [
        " -s build_type=",
        " -s os=Windows",
        " -s os_build=Windows",
        " -s arch=x86_64",
        " -s arch_build=x86_64",
        ' -s compiler="Visual Studio"',
        " -s compiler.version=16",
    ]
    targets_setup(win_targets, args)


if platform.system() == "Linux":
    lin_targets = ["WSL-GCC-Debug", "WSL-GCC-Release"]
    args = [
        " -s build_type=",
        " -s os=Linux",
        " -s os_build=Linux",
        " -s arch=x86_64",
        " -s arch_build=x86_64",
        " -s compiler=gcc",
        " -s compiler.version=9",
        " -s compiler.libcxx=libstdc++11",
    ]
    targets_setup(lin_targets, args)
