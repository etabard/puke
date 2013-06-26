#!/bin/bash
##################################################################################
# P.O.SH
# (c) 2012 Mangled Deutz <dev@webitup.fr>
# Distributed under the terms of the WTF-PL: do wtf you want with that code
##################################################################################

# Use ext glob bitch!
shopt -s extglob

ui::header(){
  tput setaf 2
  echo "********************************************************************************************"
  echo "* $@"
  echo "********************************************************************************************"
  echo ""
  tput op
}

ui::section(){
  tput setaf 2
  echo ""
  echo "____________________________________________________________________________________________"
  echo "| $@"
  echo "____________________________________________________________________________________________"
  echo ""
  tput op
}

ui::text(){
  echo "$@"
}

ui::error(){
  tput setaf 1
  echo " * ERROR: $@"
  tput op
  exit 1
}

ui::info(){
  tput setaf 2
  echo " * INFO: $@"
  tput op
}

ui::warning(){
  tput setaf 3
  echo " * WARNING: $@"
  tput op
}

ui::confirm(){
  echo "$@. Press enter now."
  read
}

ui::ask(){
  read -p "$1" $2
}


string::length(){
  poshout=${#1}
}

string::charAt(){
  poshout=${1:$2:1}
}

string::charCodeAt(){
  ch=${1:$2:1}
  ch=`echo -ne "$ch" | hexdump`
  ch=${ch:8}
  ch=${ch%%[0-9][0-9][0-9]*}
  poshout=${ch// /}
}

string::concat(){
  poshout="$1"
  shift 1
  while [[ "$#" != "" ]]; do
    poshout="${poshout}$1"
    shift 1
  done
}

string::indexOf(){
  ch=${1%%$2*}
  poshout=${#ch}
}

string::lastIndexOf(){
  ch=${1%$2*}
  poshout=${#ch}
}

string::substr(){
  poshout="${1:$2:$3}"
}


ui::header "Welcome to the puke for OSX installer"



# Do we already have puke?
if [[ "`which puke`" ]]; then
  # XXX
  # ui::error "Puke version `puke --version` is already installed. If you want to upgrade, just do: puke --upgrade"
  ui::error "Puke version XXXXXFIXME is already installed. If you want to upgrade, just do: 'puke --upgrade'. \
  If you want to uninstall, 'pip uninstall puke' as many times as necessary. \
  For more puke maintenance tasks, try 'puke --XXXFIXME'"
fi




ui::header "Checking your system now."


# No puke, so
PATH_PYTHON=`which python`
SYSTEM_PYTHON=`which /usr/bin/python`
BREW_PYTHON=`which /usr/local/bin/python`

# Eliminate versions that don't work
if [[ "$PATH_PYTHON" ]]; then
  PYTHON_VERSION=`$PATH_PYTHON -c 'import sys; print(sys.version_info[:])'`
  PV=${PYTHON_VERSION/%,*}
  if [[ "$PV" != "(2" ]]; then
    ui::warning "Found a python in your path ($PATH_PYTHON), but it's not usable (version: $PYTHON_VERSION - and we require python 2.X)"
    PATH_PYTHON=""
  fi
fi

if [[ "$SYSTEM_PYTHON" ]]; then
  PYTHON_VERSION=`$SYSTEM_PYTHON -c 'import sys; print(sys.version_info[:])'`
  PV=${PYTHON_VERSION/%,*}
  if [[ "$PV" != "(2" ]]; then
    ui::warning "Found system python ($SYSTEM_PYTHON), but it's not usable (version: $PYTHON_VERSION - and we require python 2.X)"
    SYSTEM_PYTHON=""
  fi
fi

if [[ "$BREW_PYTHON" ]]; then
  PYTHON_VERSION=`$BREW_PYTHON -c 'import sys; print(sys.version_info[:])'`
  PV=${PYTHON_VERSION/%,*}
  if [[ "$PV" != "(2" ]]; then
    ui::warning "Found a homebrew python ($BREW_PYTHON), but it's not usable (version: $PYTHON_VERSION - and we require python 2.X)"
    BREW_PYTHON=""
  fi
fi

SHOULD_FIX_PATH="false"
PYTHON_IS_SYSTEM="false"

# We have a python in path
if [[ "$PATH_PYTHON" ]]; then
  # Let assume it's custom, or homebrew python
  BEST_PYTHON="$PATH_PYTHON"
  # If it's indeed system
  if [[ "$PATH_PYTHON" == "$SYSTEM_PYTHON" ]]; then
    # But maybe we have brew somewhere
    if [[ "$BREW_PYTHON" ]]; then
      BEST_PYTHON="$BREW_PYTHON"
      SHOULD_FIX_PATH="true"
    else
      PYTHON_IS_SYSTEM="true"
    fi
  fi
else
  # So, no python in path at all :/ - let's try others
  SHOULD_FIX_PATH="true"
  if [[ "$BREW_PYTHON" ]]; then
    BEST_PYTHON=$BREW_PYTHON
  elif [[ "$SYSTEM_PYTHON" ]]; then
    BEST_PYTHON=$SYSTEM_PYTHON
    PYTHON_IS_SYSTEM="true"
  fi
fi


if [[ "$PYTHON_IS_SYSTEM" == "true" ]]; then
  ui::warning "The only python we could find is your system python. Installing puke that way is not recommended and the default from here is to install homebrew python first."
  ui::ask "If you want to use the (recommended) default using homebrew, press enter. If you are sure you want to use your system python, press S. \
  If you want to adjust your path in order to find another custom python CTRL+C now." S
  if [[ "$S" == "" ]]; then
    REQUIRE_BREW="true"
    SHOULD_FIX_PATH="true"
    BEST_PYTHON="/usr/local/bin/python"
    PYTHON_IS_SYSTEM="false"
  fi
elif [[ "$BEST_PYTHON" == "" ]]; then
  ui::warning "Couldn't find any python on your system. We will install homebrew python."
  ui::confirm "If you are sure you have python somewhere, please CTRL+C and adjust your path."
  REQUIRE_BREW="true"
  SHOULD_FIX_PATH="true"
  BEST_PYTHON="/usr/local/bin/python"
fi



if [[ "$REQUIRE_BREW" == "true" ]]; then
  # Check we have brew
  HAS_BREW=`which brew`
  if [[ "$HAS_BREW" == "" ]]; then
    ui::header "Homebrew"
    ui::confirm "Will install homebrew. Note that you NEED XCode, or XCode command line tools installed, and that we don't check for that."
    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
  fi
  ui::header "Will install homebrew python"
  ui::confirm
  brew install python
fi

if [[ "$SHOULD_FIX_PATH" == "true" ]]; then
  ui::header "PATH"
  ui::confirm "Will fix your path"
  echo 'export PATH="/usr/local/share/python:/usr/local/bin:/usr/local/sbin:$PATH"' >> ~/.profile
  source ~/.profile
fi

if [[ "$PYTHON_IS_SYSTEM" == "true" ]]; then
  ui::header "Puke"
  ui::confirm "Will install puke globally. We need to sudo!"
  sudo easy_install pip
  sudo pip install puke
  ui::info "Done!"
  exit
fi

# At that point, we are sure we have python installed, and the path is OK.
# Check for pip now

HAS_PIP=`which pip`

if [[ "$HAS_PIP" == "" ]]; then
  # Let's double check on easy_install
  HAS_EZ=`which easy_install`
  if [[ "$HAS_EZ" == "" ]]; then
    ui::error "Couldn't find easy_install! Something is terribly wrong."
  fi
  if [[ "$HAS_EZ" == "/usr/bin/easy_install" ]]; then
    ui::error "easy_install is the system one! Something is terribly wrong with the path."
  fi
  ui::header "Pip"
  ui::confirm "Will install pip"
  easy_install pip
fi

# So, we have pip... let's go
ui::header "Puke"
ui::confirm "Will install puke"
pip install puke


