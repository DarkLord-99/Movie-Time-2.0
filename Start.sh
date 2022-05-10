if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MoulikMaity/MovieTime-Robot.git /MovieTime-Robot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MovieTime-Robot
fi
cd /MovieTime-Robot
pip3 install -U -r requirements.txt
echo "Starting MovieTime RoBot...."
python3 main.py
