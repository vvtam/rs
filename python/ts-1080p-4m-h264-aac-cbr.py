#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import subprocess as sp
import os
import logging

logging.basicConfig(filename='transcode.log', level=logging.WARNING)
# logging.basicConfig(filename='tcTS.log', level=logging.INFO)


def transcode(filepath, outputdir):
    command = ["ffmpeg", "-y", "-i", filepath,
               "-loglevel",  "error",
               "-metadata", "service_name='Push Media'",
               "-metadata", "service_provider='Push Media'",
               #"-metadata", "copyright='Copyright 2018 By PM'",
               #"-metadata", "comment='An exercise in Realmedia metadata'",
               "-c:v", "h264",
               #"-vf", "scale=2*trunc(iw/2):-2,setsar=1",
               #scale args ensure an even width and height. The setsar is force a sample aspect ratio of 1 so that players don't #resize the video during display.
               "-profile:v", "high", "-level:v", "4.0",
               #"-pix_fmt", "yuv420p",
               "-x264-params", "nal-hrd=cbr",
               "-b:v", "4M", "-minrate", "4M", "-maxrate", "4M", "-bufsize", "4M",
               "-preset", "faster",
               "-s", "1920x1080",
               "-aspect", "16:9",
               "-r", "25",
               "-c:a", "aac",
               "-b:a", "192K", "-ar", "48000",
               "-f", "mpegts", "-muxrate", "6M",
               outputdir + ".ts"
               ]
    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    if pipe.returncode == 0:
        logging.info("command '%s' succeeded, returned: %s"
                     % (command, str(out)))
    else:
        logging.error("command '%s' failed, exit-code=%d error = %s"
                      % (command, pipe.returncode, str(err)))


def main():
    # 打开视频列表文件
    with open('list', 'r') as f:
        line = f.readline()
        # 逐行读取文件，并新建输出路径
        while line:
            # 输出入文件路径
            filepath = line.strip()  # 去除行尾的"\n"
            # 去除文件扩展名，获得一个list
            filedir = os.path.splitext(filepath)
            # 去除文件扩展名后的路径作为输出的路径
            outputdir = filedir[0]
            # 文件扩展名
            # filesuffix = filedir[1]
            # raise SystemExit('Debug and Exit!') #调试
            # 输出在当前目录
            outputdir = os.path.join(os.path.abspath('.'), '4m1080pts', outputdir)
            # ===输出不在当前目录===
            #output_basedir = '/mnt/nfs/transcode'
            #outputdir = os.path.join(output_basedir, 'ts8M1080P', outputdir)
            # ===输出不在当前目录===
            # 标准化路径名，合并多余的分隔符和上层引
            outputdir = os.path.normpath(outputdir)
            # 替换空格
            #outputdir = outputdir.replace(" ", "_")
            output_basedir = os.path.dirname(outputdir)
            if os.path.exists(output_basedir):
                logging.info(output_basedir + ", the dir already exist.")
            else:
                logging.info(output_basedir + ", the dir create success.")
                os.makedirs(output_basedir)
            logging.warning(filepath)  # 记录进度
            transcode(filepath, outputdir)
            line = f.readline()

if __name__ == '__main__':
    main()
