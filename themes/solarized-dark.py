class Color(DefaultColor):
    base03  =  8
    base02  =  0
    base01  = 10
    base00  = 11
    base0   = 12
    base1   = 14
    base2   =  7
    base3   = 15
    yellow  =  3
    orange  =  9
    red     =  1
    magenta =  5
    violet  = 13
    blue    =  4
    cyan    =  6
    green   =  2

    USERNAME_FG = base0
    USERNAME_BG = base02
    USERNAME_ROOT_BG = red

    HOSTNAME_FG = base0
    HOSTNAME_BG = base03

    HOME_SPECIAL_DISPLAY = False
    PATH_FG = base03
    PATH_BG = blue
    CWD_FG = base03
    SEPARATOR_FG = base1

    READONLY_BG = red
    READONLY_FG = base03

    REPO_CLEAN_FG = base03
    REPO_CLEAN_BG = yellow
    REPO_DIRTY_FG = base03
    REPO_DIRTY_BG = yellow

    JOBS_FG = cyan
    JOBS_BG = base02

    CMD_PASSED_FG = base3
    CMD_PASSED_BG = green
    CMD_FAILED_FG = base3
    CMD_FAILED_BG = red

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    VIRTUAL_ENV_BG = green
    VIRTUAL_ENV_FG = base03

    GIT_AHEAD_BG = base02
    GIT_AHEAD_FG = yellow
    GIT_BEHIND_BG = base02
    GIT_BEHIND_FG = yellow
    GIT_STAGED_BG = base02
    GIT_STAGED_FG = yellow
    GIT_NOTSTAGED_BG = base02
    GIT_NOTSTAGED_FG = yellow
    GIT_UNTRACKED_BG = base02
    GIT_UNTRACKED_FG = yellow
    GIT_CONFLICTED_BG = base02
    GIT_CONFLICTED_FG = yellow

    SALTENV_FG = base03
    SALTENV_BG = orange

    SSH_FG = base03
    SSH_BG = cyan
