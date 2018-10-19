#!/usr/bin/env bash
DATE=$(date +%F)
FILE=CHANGELOG.md
echo "#CHANGELOG ON" $DATE > $FILE

git log --no-merges --format="%cd" --date=short --no-merges --all | sort -u -r | while read DATE ; do
  if [[ $NEXT != "" ]]
  then
    echo >> $FILE
    echo "###" $NEXT >> $FILE
  fi
  GIT_PAGER=cat git log --no-merges --format="    * %s" --since=$DATE --until=$NEXT --all >> $FILE
  NEXT=$DATE
done

sed -i'' -E 's!\#([[:digit:]]*)![#\1]\(../../pull/\1\)!g' CHANGELOG.md
