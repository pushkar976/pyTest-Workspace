#!/bin/bash

sftp -i ubuntu@TEST_SERVER <<EOF
cd /home/ane/data/uploads/deals/
put /home/pushkar/Workspace/core-automation/automate_sftp/52913_FYI_toyota1_advertiser_08162021_09052021_md5sum_53d1a15a006dcaba010ca9f1605ee428.xml
EOF
