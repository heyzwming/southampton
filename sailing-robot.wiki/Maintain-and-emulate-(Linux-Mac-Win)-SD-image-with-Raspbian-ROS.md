# Generate a new image
(see samepage, firmware section)
* ```dd bs=4M if=/dev/whereverSDcard of=/path/to/img/file.img; sync```
* Can be easily compressed to about ~2Gb

# Flash current image copy
* download current image copy from sailing robot google drive https://drive.google.com/open?id=0B0Wl35F24aqXUUdLUVBCVzlTZnc
* copy current image onto SD card: ``` dd if=/path/to/img/file.img of=/dev/theSDcardDevice bs=4M; sync```
* update launch scripts, firmware
* **Alternatively** use flash tool for RPi https://github.com/hypriot/flash

# Shrink the image
If the SD card is smaller than the one used for the backup you can shrink the image before the copy, everything is explained here: http://softwarebakery.com/shrinking-images-on-linux . 

If needed one can delete some files first (rosbags for example) by mounting the image locally.

``` sudo mount -o loop path/to/img/file.img somewhere/to/mount ```

# QEMU emulator (Linux/Mac/Win)
(following <https://github.com/dhruvvyas90/qemu-rpi-kernel/wiki/Emulating-Jessie-image-with-4.x.xx-kernel>)

* Needs a ```.img``` file from the RPi and a [ARM kernel](https://github.com/dhruvvyas90/qemu-rpi-kernel), `kernel-qemu-4.4.13-jessie` in our case. Currently these files are in Tabarly: `~/kernel-qemu-4.4.13-jessie` and `~/SDCardBack28March17.img`. `~/rpi_image` is an empty folder that can be used to mount the `.img` file to get the emulator ready.
* Comment out a few lines as explained in the article.
* Launch the emulator `qemu-system-arm -kernel ~/kernel-qemu-4.4.13-jessie -cpu arm1176 -m 256 -M versatilepb -serial stdio -append "root=/dev/sda2 rootfstype=ext4 rw" -hda ~/SDCardBack28March17.img`
