cd smplify-x
pip install -r requirements.txt

# For specific branch 'cvpr19' of human_body_prior
cd human_body_prior
python setup.py install

cd openpose-docker
sudo docker build -t openpose .
sudo docker run --gpus 0 --network host --name openpose -it openpose_v1:latest /bin/bash

# Note:
# Copy the `models` folder under `openpose` into docker container

# Inside docker container
cd /openpose
mkdir build && cd build
cmake .. -DBUILD_PYTHON=ON -DUSE_CUDNN=OFF .. && make -j`nproc`
./build/examples/openpose/openpose.bin --video examples/media/video.avi --write_json output/ --display 0 --render_pose 0 --model_folder models/
# Or anyway you want to deal with your data

# Copy the output json files to the host machine
sudo docker cp openpose:/openpose/output_json ./content/keypoints

# Return to host machine
cd smplify-x

# For me
python smplifyx/main.py --config cfg_files/fit_smplh.yaml 
   --data_folder ../content/images 
   --output_folder ../content/output
   --visualize="True"
   --model_folder ../content/models
   --vposer_ckpt ../content/vposer
# for which my smplh models are merged by smplx/tools/merge_smplh_mano.py