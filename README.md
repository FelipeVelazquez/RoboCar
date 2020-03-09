<h1> RoboCar<h1 /> <br />
<h2 > Comandos para secuencia de ejecución <h2 />
<h3> Instalacion de recursos previos <h3 />
<ul>
  <li>sudo apt-get install ros-melodic-octomap<li />
<ul />
<h3> Comandos para ejecucion <h3 />
<ol>
  <li>roslaunch openni_launch openni.launch<li />
  <li>roslaunch pointcloud_to_laserscan start.launch<li />
  <li >rosrun odometria Odometria_Xbox.py<li />
  <li >rosrun gmapping slam_gmapping scan:=camera/scan<li />
  <li >roslaunch octomap_server octomap_mapping.launch <li />
<ol />
