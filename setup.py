import commands
import os
import os.path

def instal_hs(path_to_repo, path):
    if not path_to_repo == "":
        os.chdir(path_to_repo)
    install = commands.getstatusoutput('cabal install --bindir="%s"' % path)
    print install[1]
    return install[0]
    
def main():
    current_path = os.path.abspath(os.curdir)
    bin_path = os.path.join(current_path, "bin")
    print commands.getstatusoutput('git submodule update --init --recursive')[1]
    print current_path
    """paths_to_repos = ["abolute/path/to/csv2sql/repo"
                    , "abolute/path/to/csvLoader/repo"
                    , "abolute/path/to/stablePortfolio/repo"
                  ]
    """
    rel_paths_to_dirs = filter (os.path.isdir, os.listdir(current_path))
    paths_to_repos = map (os.path.abspath, rel_paths_to_dirs)
    for path in paths_to_repos:
        print path
        instal_hs(path, bin_path)

if __name__ == "__main__":
    main()
