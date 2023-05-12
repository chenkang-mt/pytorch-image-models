import subprocess

cmd = "python train.py /home/kangchen/tiny-imagenet/tiny-imagenet-200/ \
    --model efficientnetv2_rw_t \
    --img-size 288 -b 128 \
    --device musa \
    --sched step \
    --epochs 450 \
    --decay-epochs 2.4 \
    --decay-rate .97 \
    --opt rmsproptf \
    --opt-eps .001 \
    -j 4 \
    --warmup-lr 1e-6 \
    --weight-decay 1e-5 \
    --drop 0.3 \
    --drop-path 0.2 \
    --model-ema \
    --model-ema-decay 0.9999 \
    --aa rand-m9-mstd0.5 \
    --remode pixel \
    --reprob 0.2 \
    --lr .016".split()

res = subprocess.call(cmd)
print(res)