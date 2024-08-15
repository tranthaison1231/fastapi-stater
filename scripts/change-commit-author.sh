#!/bin/sh
git filter-branch --env-filter '

OLD_EMAIL="son.tran@enouvo.com"          # <- change this
CORRECT_NAME="Son Tran"             # <- change this
CORRECT_EMAIL="son.tran@gmail.com"  # <- change this

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi

if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags HEAD~5..HEAD
