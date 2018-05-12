SyncShell  [![Build Status](https://img.shields.io/travis/msudgh/syncshell/master.svg?style=flat)](https://travis-ci.org/msudgh/syncshell)  [ ![MIT License](https://img.shields.io/badge/license-MIT-brightgreen.svg) ](https://mit-license.org/msudgh)  [ ![PyPi](https://img.shields.io/github/release/msudgh/syncshell.svg) ](https://github.com/msudgh/syncshell/releases)  [![PyPi](https://img.shields.io/pypi/v/syncshell.svg)](https://pypi.org/project/syncshell/)
=========
  > **Yet another tool for laziness**

Keep your machine's shell history synchronize

## Get SyncShell
Currently, `SyncShell` is just available on `PyPi` and by the following command install the latest version:
```bash
$ pip install syncshell # Maybe sudo need
```
```bash
$ syncshell -- --help
Type:        Syncshell

Usage:       syncshell 
             syncshell auth
             syncshell download
             syncshell upload
```

## Requirements
 * Python 3+

## How it Works
The actual idea of SyncShell is synchronization of your devices shell history, Almost, this ability will be useful when you want to sync your office and home machines. SyncShell is just built on Github `Gist` feature such that this CLI tool represents three methods to communicate with the tool.

According to Github API, you can generate a token key with `gist` scope to accessing to your gists. Gists have two **`public`**, **`secret`** type which syncshell while executing `syncshell upload` command will use secret type to store your history file and keep them secret on Github Gist.

On the others machine, by executing `syncshell download` after entering your token key and created Gist ID you can download the gist and sync your shell's history.

  > Gists will be secret until you don't share it with someone else, In other words, It'll be secret and safe until you only have the Github Token and Gist ID.

## Usage
  > Currently, `SyncShell` just support `zsh` and supporting other shells is in WIP.

Before SyncShell can be useful you need to setup your Github token key:

  1. Open [**Github personal access tokens**](https://github.com/settings/tokens) page, [**Generate a new token**](https://github.com/settings/tokens/new) with `gist` scope feature.
  2. Execute the **`syncshell auth`** command, Enter your token key to validate and confirm it.
  3. Done :wink:

Now you can try to upload your shell history by the following command:

```bash
$ syncshell upload
```

After the uploading process, you'll take a Gist ID that by this ID and your Github token, you can download history on the others machine by executing the following command:
```bash
$ syncshell download
```

## Todo
- [ ] Write more test cases
- [ ] Support `bash` and other shells

## Contributing
So nice you wanna contribute to this repository. Thank you. You may contribute in several ways like:

  * Creating new features
  * Fixing bugs
  * Write test cases

#### Installing dependencies
By the following command install syncshell dependencies
```bash
$ python install -r requirements.txt
```

#### Tests
Before submiting your PR, Execute the below command to be sure about passing test cases.
```bash
$ pytest -c pytest.ini -s
```

Done :wink:

## License
The code is licensed under the MIT License. See the data's [LICENSE](https://github.com/msudgh/syncshell/blob/master/LICENSE) file for more information.
