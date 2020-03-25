# Conan recipe for the MatchPoint framework

This project uses [Conan][conan] to download [MatchPoint][matchpoint] and build it using CMake. [ITK][itk] is required as a dependency and is also downloaded and built using Conan and CMake.

## Getting started

### Prerequisites - Setting up Conan
To install Conan (tested with Conan 1.22), see the [Conan documentation][conan-doc]. It is recommended to use a [virtual environment][venv] with python.

After you activated your virtual environment and installed Conan (see [install packages][venv-active]), check if Conan is set up correctly by typing `conan`.
Conan should have automatically set up a remote repository, the [Conan center][conan-center]. If you type

```
conan remote list
```

you will get a list of all your remote repositories. For a new install this should be:

```
WARN: Remotes registry file missing, creating default one in [...]remotes.json
conan-center: https://conan.bintray.com [Verify SSL: True]
```

If you type 

```
conan search matchpoint
```

you will get the message

```
There are no packages matching the 'matchpoint' pattern
```

which means that no MatchPoint package is found in your local cache.

### Installing - ITK as dependency
MatchPoint requires ITK as dependency (or [requirement](matchpoint/conanfile.py#L17)). A Conan recipe for installing ITK as a local Conan package is included in this repository: The [conanfile.py](itk/conanfile.py) describes the configuration and build steps for the ITK package. To install this package into your local cache, change to the `itk`-directory in your local copy of this repository and type

```
conan create .
```

`.` refers to the current directory so this only works if the command is called from withing the `itk`-directory.
This will configure and build ITK using CMake, given the [CMake definitions](itk/conanfile.py#L22-L32) of the recipe. Additionally a simple test is performed using this [conanfile.py](itk/test_package/conanfile.py). After building, packaging and testing the ITK package, you will see this output:

```
itk/4.13.2 (test package): Calling build()

[...]

itk/4.13.2 (test package): Running test()
Test
```

For more information about Conan packages, see [Creating Packages][conan-package].

To see if everything worked well, you can type

```
conan search itk
```

to get an output like this:

```
Existing package recipes:

itk/4.13.2
```

You have now successfully installed ITK 4.13.2 into your local cache.

### Installing - MatchPoint
If the package `itk/4.13.2` exists in your local cache, you can install the MatchPoint package by changing to the `matchpoint`-directory and typing 

```
conan create .
```
`.` refers to the current directory so this only works if the command is called from withing the `matchpoint`-directory.
This will configure and build MatchPoint using CMake, given the [CMake definitions](matchpoint/conanfile.py#L33-L35) of the recipe.

To see if everything worked well, you can type

```
conan search matchpoint
```

to get an output like this:

```
Existing package recipes:

matchpoint/0.1
```

You have now successfully installed MatchPoint into your local cache.


[conan]: https://conan.io/
[matchpoint]: https://github.com/MIC-DKFZ/MatchPoint
[itk]: https://github.com/InsightSoftwareConsortium/ITK
[conan-doc]: https://docs.conan.io/en/1.22/installation.html#install-with-pip-recommended
[venv]: https://docs.python.org/3/library/venv.html
[venv-active]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
[conan-center]: https://conan.io/center/
[conan-package]: https://docs.conan.io/en/1.22/creating_packages/getting_started.html
