------------------------------------------------------------ Application manager ----------------------------------------

## Goal / Utilities

- **Download and install applications (scripts, appImages, zip files containing other files...)**
- **Check information about installed apps**
- **Remove apps or update them**

### Downloading and installing applications

The app manager should be able to download files from the Internet. It should also be able to handle all kinds 

of errors than happened during that procedure:

- **Internet unavailable**
- **Resource not found**
- **Unknown error**

For installing applications, the app manager will ask from the user what do:

### Pro download procedure

- Ask for the name of the program, and its version, and if it is a CLI program

- Ask from the user what kind of application it is (folder: d, executable: exe, script: s, zip file: z)

  | Application type       | directory                                                    | executable                                                   | script                                                       | zip file                                                     |
  | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | **First instruction**  | show to tree of the folder                                   | Move the executable to its destination                       | Move the script to its destination                           | extract to .temp_app and show to tree                        |
  | **Second instruction** | Ask the user user to give the path of the main executable    | Ask the user to give the command for it to run               | Ask the user to give the command for it to run               | Ask the user to give the path of the main executable         |
  | **Third instruction**  | Ask to user to give the command for it to run                | Ask the user whether it needs a desktop file or not          | Ask the user if it needs a desktop file or not               | Ask the user to give the command for it to run               |
  | **Fourth instruction** | Ask to user whether it needs a desktop file or not           | Create a local manifest for the app & add the app to the global manifest | Create a local manifest for the app & add the app to the global manifest | Ask to user whether it needs a desktop file or not           |
  | **Fifth instruction**  | Move the folder to its destination                           | -                                                            | -                                                            | Move the folder to its destination                           |
  | **Sixth instruction**  | Create a local manifest for the app & add the app to the global manifest | -                                                            | -                                                            | Create a local manifest for the app & add the app to the global manifest |

- ### Desktop file creation

  - Open a file at the $user/local/applications/$app_name.desktop

  - add the name and the version

  - | Properties | Icon                                            | Aliases                           | terminal        |
    | ---------- | ----------------------------------------------- | --------------------------------- | --------------- |
    | **Demand** | ask the user to give the path of an icon or URL | ask the user to give some aliases | `terminal=$cli` |


- ### Local manifest creation & schema

	- Create a file called manifest.mf at $app_location

  | Name         | Version            | Execution            |
  | ------------ | ------------------ | -------------------- |
  | `name=$name` | `version=$version` | `exec=$exec_command` |


- ### Adding the app to the global manifest

  - The global manifest is a binary file containing python dictionaries

  - The schema of this dictionary is:

    `{name: $name, path: $path}`

    

# Global

applications path: ($*appmgr_location*/apps/$*appname*)