#!/bin/bash

number=0

while true; do

finished=0

# sure you can work out a better way!
#for i in {0..500}; do
#  if [ $finished == 0 ]; then
#    if [ ! -e ./photos/photo$i.jpg ]; then
#      number=$i
#      finished=1
#    fi
#  fi
#done

function countdown {
    eog --single-window ./slides/3.png -f &
    sleep 1
    eog --single-window ./slides/2.png -f &
    sleep 1
    eog --single-window ./slides/1.png -f &
    sleep 1
    eog --single-window ./slides/black.png -f &
}

eog --single-window ./slides/start.png -f &
sleep 1
wmctrl -a 'abeverley@andy-laptop: ~/git/photobooth'
read -n 1 -p "press any key!"
# rm *.jpg

countdown

file1=`mktemp photos/XXXXXXXX.jpg`
gphoto2 --capture-image-and-download --force-overwrite --filename $file1
countdown
file2=`mktemp photos/XXXXXXXX.jpg`
gphoto2 --capture-image-and-download --force-overwrite --filename $file2
countdown
file3=`mktemp photos/XXXXXXXX.jpg`
gphoto2 --capture-image-and-download --force-overwrite --filename $file3
countdown
file4=`mktemp photos/XXXXXXXX.jpg`
gphoto2 --capture-image-and-download --force-overwrite --filename $file4
eog --single-window ./slides/loading.png -f &

# gphoto2 --get-all-files
rm -f photo.jpg
mogrify -path . -format JPG -resize 50% $file1 $file2 $file3 $file4
montage -mode concatenate -tile 2x2 $file1 $file2 $file3 $file4 photo.jpg

eog --single-window photo.jpg -f &
# scp photo.jpg mark@192.168.0.104:/home/mark/Desktop &
rm -f IMG*
# gphotofs temppic
# rm ./temppic/DCIM/*/*
# fusermount -u ./temppic
sleep 6
killall eog
# cp photo.jpg ./photos/photo$number.jpg
# scp ./photos/photo$number.jpg pi@192.168.0.105:/home/pi/Pictures &
done

