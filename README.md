# Resources

[Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/)

[Lecture 6: Version Control (git) (2020)](https://www.youtube.com/watch?v=2sjqTHE0zok)

[How to ignore certain files in Git](https://stackoverflow.com/questions/4308610/how-to-ignore-certain-files-in-git)

[How can I create a Git repository with the default branch name other than "master"?](https://stackoverflow.com/questions/42871542/how-can-i-create-a-git-repository-with-the-default-branch-name-other-than-maste)

[How to change the URI (URL) for a remote Git repository?](https://stackoverflow.com/questions/2432764/how-to-change-the-uri-url-for-a-remote-git-repository)

# Intro

Version Control are tools to keep track of the history changes done to source code / collections of files or folders (in a series of snapshots + metadata, e.g. author, date and timestamp of a change or messages) > facilitate collaboration and allows the user to: 

- look at old version of source code
- reasons for change
- work in parallel w/out conflicts
- work on different features or bugs while keeping other features independent
- resoving conflicts
- sending patches and modules of codes around

# Files and Folders Abstraction Model

```
<root> (tree)
|
+- foo (tree)
|  |
|  + bar.txt (blob, contents = "hello world")
|
+- baz.txt (blob, contents = "git is wonderful")
```

Recursive data structure (i.e. data structure that is partially composed of smaller of simpler instances of the same data structure): tree can contain other trees (and blobs)

The root is the directory being tracked, i.e. folder on your computer corresponding to a software project

Directory: file which consists solely of a set of other files

# Modeling History

History can be modeled as a linear sequence of snapshots (i.e. all the files and folders in the project + metadata) > git uses a directed acyclic graph to model history > every new state points to the previous state in the graph

## Snapshots / Commits

```
o <-- o <-- o <-- o (base project + new feature)
            ^
             \
              --- o <-- o (bug fix)
```

Afterwards we can merge both forks and create a new state

```
o <-- o <-- o <-- o <-- o (base project + new feature + bug fixes)
            ^         /
             \       /
              -- o < 
```

(Merge conflicts = concurrent changes in the new state)

# Data Structure / Model of History

```
// a file is a bunch of bytes
type blob = array<byte>

// a directory contains named files and directories
type tree = map<string, tree | blob>

// a commit has parents, metadata, and the top-level tree
type commit = struct {
    parent: array<commit>
    author: string
    message: string
    snapshot: tree
}

// this are only references. For storage and distribution we use objects
```

# Objects and Content-Addressing

```
type object = blob | tree | commit
```

All objects are [content-addressed](https://en.wikipedia.org/wiki/Content-addressable_storage) > what git maintains is a set of objects in disk

```
objects = map<string, object> 
(objects = map<id, object>)

def store(object):
    id = sha1(object)
    objects[id] = object

def load(id):
    return objects[id]
```

We now can name the objects in the commits graph

Git maintains a set of objects and a set of references > a git repository stores objects and references

# References

Git maintains a set of objects and a set of references

```
//human readable name to object id
references = map<string, string>

def update_reference(name, id):
    references[name] = id

def read_reference(name):
    return references[name]

def load_reference(name_or_id):
    if name_or_id in references:
        return load(references[name_or_id])
    else:
        return load(name_or_id)
```

The graph is immutable, references are mutable

Git commands manipulates the references data or objects data

# Collaboration

git 

# Misc

- Git does not track empty directories

[git still shows files as modified after adding to .gitignore](https://stackoverflow.com/questions/9750606/git-still-shows-files-as-modified-after-adding-to-gitignore)

[git still shows files as modified after adding to .gitignore](https://stackoverflow.com/questions/9750606/git-still-shows-files-as-modified-after-adding-to-gitignore)

[gitignore.io](https://www.toptal.com/developers/gitignore)