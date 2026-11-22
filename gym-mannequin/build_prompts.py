#!/usr/bin/env python3
"""Sinh prompt sẵn dán cho 60 bài tập: python3 build_prompts.py  -> prompts/ + exercises.csv"""
import csv, os, re, unicodedata

# (nhóm, bài tập + máy [EN], cơ mục tiêu [EN], tên VN, cơ VN, lưu ý form VN)
EX = [
("Ngực","Barbell Bench Press on a flat bench","pectoralis major (chest)","Đẩy tạ đòn nằm ngang","ngực giữa","Siết bả vai về sau, hạ thanh xuống ngực, đẩy lên mà không khóa khuỷu."),
("Ngực","Incline Dumbbell Press on an incline bench","upper chest (clavicular head of pectoralis major)","Đẩy tạ đơn ghế dốc","ngực trên","Ghế dốc khoảng ba mươi độ, khuỷu chếch nhẹ, đẩy lên rồi siết ngực."),
("Ngực","Dumbbell Fly on a flat bench","pectoralis major (chest)","Ép tạ đơn nằm ngang","ngực","Giữ khuỷu hơi cong, mở ngực vừa đủ rồi ôm tạ về như ôm một thân cây."),
("Ngực","Cable Crossover on a cable machine","pectoralis major (chest)","Kéo cáp chéo ngực","ngực","Bước lên một chân, kéo hai tay chụm trước ngực và giữ một nhịp siết."),
("Ngực","Seated Chest Press Machine","pectoralis major (chest)","Máy đẩy ngực ngồi","ngực","Lưng áp ghế, đẩy ra không khóa khuỷu, về chậm để cảm nhận ngực giãn."),
("Ngực","Pec Deck Machine Fly","pectoralis major (chest)","Máy ép ngực","ngực","Ngực ưỡn, vai hạ thấp, ép hai tay vào giữa và dừng một nhịp."),
("Ngực","Push-Up on the gym floor","pectoralis major (chest)","Hít đất","ngực","Thân thẳng như tấm ván, hạ ngực sát sàn, khuỷu chếch khoảng bốn lăm độ."),
("Ngực","Decline Bench Press","lower chest (sternal head of pectoralis major)","Đẩy tạ ghế dốc xuống","ngực dưới","Hạ thanh xuống phần ngực dưới, kiểm soát nhịp, đẩy lên thẳng trục."),
("Lưng","Lat Pulldown on a cable machine","latissimus dorsi","Kéo xô cáp","cơ xô","Ưỡn ngực, kéo khuỷu xuống túi quần, không giật người ra sau."),
("Lưng","Pull-Up on a pull-up bar","latissimus dorsi","Kéo xà đơn","cơ xô","Bắt đầu bằng hạ bả vai, kéo cằm qua xà, hạ xuống chậm hết tầm."),
("Lưng","Seated Cable Row","rhomboids and middle trapezius (mid back)","Kéo cáp ngồi","lưng giữa","Ngực cao, kéo khuỷu ra sau và siết hai bả vai lại với nhau."),
("Lưng","Barbell Bent-Over Row","latissimus dorsi and mid back","Kéo tạ đòn cúi người","lưng xô và lưng giữa","Lưng thẳng, gập hông, kéo thanh về rốn và hạ có kiểm soát."),
("Lưng","One-Arm Dumbbell Row on a flat bench","latissimus dorsi","Kéo tạ đơn một tay","cơ xô","Kéo khuỷu về phía hông, không xoay người, dừng một nhịp ở trên."),
("Lưng","T-Bar Row machine","mid back (rhomboids, middle trapezius)","Kéo T-bar","lưng giữa","Giữ lưng phẳng, kéo tay cầm về ngực dưới và siết bả vai."),
("Lưng","Straight-Arm Pulldown on a cable machine","latissimus dorsi","Kéo cáp tay thẳng","cơ xô","Tay gần thẳng, đẩy thanh xuống về đùi, cảm nhận xô co lại."),
("Lưng","Conventional Barbell Deadlift","erector spinae (lower back) and glutes","Deadlift","lưng dưới và mông","Thanh sát chân, lưng trung lập, đẩy sàn bằng chân rồi khóa hông."),
("Lưng","Face Pull on a cable machine with rope","rear deltoids and upper back","Kéo cáp về mặt","vai sau và lưng trên","Kéo dây về tầm trán, xoay ngoài hai bàn tay, siết vai sau."),
("Vai","Seated Dumbbell Shoulder Press","anterior and lateral deltoids","Đẩy vai tạ đơn ngồi","vai","Lưng áp ghế, đẩy thẳng lên trên đầu, không ưỡn lưng thái quá."),
("Vai","Standing Dumbbell Lateral Raise","lateral deltoid","Nâng tạ đơn sang ngang","vai giữa","Nâng khuỷu ngang vai, hạ chậm, đừng nhún vai để lấy đà."),
("Vai","Standing Dumbbell Front Raise","anterior deltoid","Nâng tạ đơn ra trước","vai trước","Nâng đến ngang vai, thân người đứng yên, hạ xuống chậm."),
("Vai","Reverse Pec Deck Machine","rear deltoid","Máy ép ngược vai sau","vai sau","Ngực tựa đệm, mở hai tay ra sau, nghĩ tới việc kéo bằng khuỷu."),
("Vai","Barbell Shrug","upper trapezius","Nhún vai tạ đòn","cơ cầu vai","Nhún thẳng lên tai, dừng một nhịp, không xoay vai."),
("Vai","Seated Arnold Press with dumbbells","deltoids","Arnold press","vai","Xoay bàn tay từ hướng mặt sang hướng trước khi đẩy lên."),
("Vai","Single-Arm Cable Lateral Raise","lateral deltoid","Nâng cáp sang ngang","vai giữa","Cáp thấp, nâng khuỷu dẫn đầu và giữ căng liên tục."),
("Tay trước","Standing Barbell Curl","biceps brachii","Cuốn tạ đòn","tay trước","Khuỷu cố định sát thân, cuốn lên siết cơ, hạ xuống chậm."),
("Tay trước","Incline Dumbbell Curl on an incline bench","biceps brachii (long head)","Cuốn tạ đơn ghế dốc","đầu dài tay trước","Tay buông thẳng sau thân người để cơ giãn tối đa rồi cuốn lên."),
("Tay trước","Standing Hammer Curl with dumbbells","brachialis and brachioradialis","Cuốn tạ búa","cơ cánh tay và cẳng tay","Giữ lòng bàn tay đối nhau, cuốn lên mà không đung đưa người."),
("Tay trước","Preacher Curl on a preacher bench","biceps brachii","Cuốn tạ ghế preacher","tay trước","Tì chặt cánh tay lên đệm, hạ hết tầm nhưng không bật nảy."),
("Tay trước","Cable Curl with straight bar","biceps brachii","Cuốn cáp","tay trước","Khuỷu sát hông, cáp giữ lực căng suốt cả nhịp."),
("Tay sau","Triceps Rope Pushdown on a cable machine","triceps brachii","Đẩy cáp dây tay sau","tay sau","Khuỷu sát thân, đẩy xuống rồi tách dây ra hai bên ở cuối."),
("Tay sau","Overhead Dumbbell Triceps Extension","triceps brachii (long head)","Duỗi tay sau qua đầu","đầu dài tay sau","Khuỷu chỉ về phía trước, hạ tạ sau đầu rồi duỗi hết tay."),
("Tay sau","EZ-Bar Skull Crusher on a flat bench","triceps brachii","Skull crusher","tay sau","Chỉ gập khuỷu, hạ thanh về trán và duỗi lên không mở khuỷu."),
("Tay sau","Close-Grip Bench Press","triceps brachii","Đẩy tạ tay hẹp","tay sau","Hai tay rộng bằng vai, khuỷu sát thân, đẩy lên bằng lực tay sau."),
("Tay sau","Bench Dip","triceps brachii","Dip ghế","tay sau","Lưng sát ghế, hạ vai vừa phải, đẩy lên bằng tay sau."),
("Chân","Barbell Back Squat in a squat rack","quadriceps and glutes","Squat tạ đòn","đùi trước và mông","Siết bụng, gối theo hướng mũi chân, xuống ngang gối rồi đẩy sàn lên."),
("Chân","Leg Press machine","quadriceps","Đạp đùi máy","đùi trước","Lưng sát đệm, hạ sâu vừa đủ, không khóa gối ở trên."),
("Chân","Leg Extension machine","quadriceps","Máy đá đùi trước","đùi trước","Duỗi hết gối, siết đùi một nhịp, hạ xuống thật chậm."),
("Chân","Romanian Deadlift with barbell","hamstrings","Romanian deadlift","đùi sau","Đẩy hông ra sau, thanh sát chân, hạ đến khi đùi sau căng."),
("Chân","Seated Leg Curl machine","hamstrings","Máy gập đùi sau ngồi","đùi sau","Cuốn gót về phía mông, siết một nhịp, thả về chậm."),
("Chân","Lying Leg Curl machine","hamstrings","Máy gập đùi sau nằm","đùi sau","Hông áp đệm, cuốn gót lên và không nhấc hông."),
("Chân","Bulgarian Split Squat with dumbbells","quadriceps and glutes","Squat tách chân kiểu Bulgaria","đùi trước và mông","Thân hơi nghiêng, hạ thẳng xuống, đẩy bằng gót chân trước."),
("Chân","Walking Lunges with dumbbells","quadriceps and glutes","Chùng chân đi bộ","đùi và mông","Bước dài vừa phải, gối sau chạm nhẹ sàn, thân người thẳng."),
("Chân","Hack Squat machine","quadriceps","Hack squat","đùi trước","Lưng sát đệm, hạ có kiểm soát, đẩy lên bằng toàn bàn chân."),
("Chân","Goblet Squat with a kettlebell","quadriceps and glutes","Goblet squat","đùi trước và mông","Ôm tạ trước ngực, ngực cao, xuống sâu và giữ gót chạm sàn."),
("Mông","Barbell Hip Thrust with upper back on a bench","gluteus maximus","Hip thrust","cơ mông","Cằm hơi cúi, đẩy hông lên khóa mông, xương sườn không bung."),
("Mông","Cable Glute Kickback with ankle strap","gluteus maximus","Đá mông với cáp","cơ mông","Giữ hông cố định, đá gót ra sau và siết mông ở cuối."),
("Mông","Seated Hip Abduction machine","gluteus medius","Máy mở háng ngồi","mông giữa","Ngả người nhẹ về trước, mở chân chậm và giữ một nhịp."),
("Mông","Glute Bridge on a mat","gluteus maximus","Cầu mông","cơ mông","Chân đặt gần mông, đẩy gót lên và siết mông ở trên."),
("Bắp chân","Standing Calf Raise machine","gastrocnemius (calves)","Nhón gót đứng","bắp chân","Hạ gót thật sâu, nhón lên cao nhất và dừng một nhịp."),
("Bắp chân","Seated Calf Raise machine","soleus (calves)","Nhón gót ngồi","bắp chân dưới","Gối gập chín mươi độ, nhón chậm và giữ căng ở đỉnh."),
("Bụng","Kneeling Cable Crunch","rectus abdominis (abs)","Gập bụng cáp","cơ bụng","Cuộn xương sườn về phía hông, không kéo bằng tay."),
("Bụng","Hanging Leg Raise on a pull-up bar","lower abs (rectus abdominis)","Treo xà nâng chân","bụng dưới","Cuộn xương chậu lên, nâng chân có kiểm soát, không đung đưa."),
("Bụng","Forearm Plank on a mat","core (rectus abdominis and transverse abdominis)","Plank","cơ core","Mông và bụng siết chặt, thân thẳng, thở đều."),
("Bụng","Russian Twist with a weight plate","obliques","Xoay người kiểu Nga","cơ liên sườn","Xoay bằng ngực chứ không chỉ bằng tay, lưng giữ thẳng."),
("Bụng","Ab Wheel Rollout on a mat","rectus abdominis (abs)","Lăn bánh xe bụng","cơ bụng","Siết bụng, lăn ra vừa tầm rồi kéo về bằng bụng."),
("Bụng","Decline Sit-Up on a decline bench","rectus abdominis (abs)","Gập bụng ghế dốc","cơ bụng","Cuộn người từng đốt lên, không giật cổ, hạ xuống chậm."),
("Tay cẳng","Seated Dumbbell Wrist Curl","forearm flexors","Cuốn cổ tay","cẳng tay","Cẳng tay tựa đùi, chỉ cử động cổ tay, biên độ trọn vẹn."),
("Toàn thân","Farmer's Carry with heavy dumbbells","forearms and upper trapezius","Đi bộ cầm tạ","cẳng tay và cơ cầu vai","Ngực cao, vai kéo xuống, bước đều và siết chặt tay cầm."),
("Lưng","Back Extension on a Roman chair","erector spinae (lower back)","Gập lưng ghế La Mã","lưng dưới","Hông cố định, hạ thân có kiểm soát, nâng đến thẳng hàng rồi dừng."),
("Bụng","Cable Woodchop on a cable machine","obliques","Chặt cáp chéo","cơ liên sườn","Xoay từ hông và thân, tay làm cầu nối, chân vững."),
]
assert len(EX) == 60

POSE = ('"Consistent character, exact same matte white faceless muscular mannequin wearing black sweatpants as the uploaded reference image. '
        'The mannequin is performing {ex} in a dark modern gym with black equipment. The mannequin\'s {m} is glowing intense neon red. '
        'High contrast, photorealistic, clean cinematic lighting, monochrome aesthetic, exact character match, 8k resolution."')
ANIM = ('"Perfectly animate the uploaded image. The matte white faceless muscular mannequin in black sweatpants executes a {ex}. '
        'The movement is highly realistic, fluid, and biomechanically accurate, demonstrating perfect gym form and a full range of motion. '
        'The primary target muscle for this exercise glows intense neon red, visibly contracting and stretching naturally with the movement. '
        'The surrounding gym equipment and dark environment remain completely stable and consistent. '
        'Cinematic lighting, slow controlled motion, photorealistic 8k video."')
SIDE = " Camera: {cam}."
CAMS = ["static side view, full body", "static front three-quarter view, full body", "slow push-in close-up on the glowing target muscle"]

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

os.makedirs("prompts", exist_ok=True)
with open("exercises.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["#", "nhom", "bai_tap_en", "co_muc_tieu_en", "ten_vn", "loi_thoai_vn"])
    for i, (g, ex, m, vn, mvn, cue) in enumerate(EX, 1):
        voice = f"{vn}. Bài này tập {mvn}. {cue}"
        w.writerow([i, g, ex, m, vn, voice])
        clips = "\n\n".join(f"**Clip {k+1}** (thêm vào cuối prompt):\n```\n{ANIM.format(ex=ex)}{SIDE.format(cam=c)}\n```" for k, c in enumerate(CAMS))
        open(f"prompts/{i:02d}-{slug(ex)[:40]}.md", "w", encoding="utf-8").write(
f"""# {i:02d}. {vn} — {ex}
Nhóm: {g} | Cơ mục tiêu: {m} ({mvn})

## Bước 1 — Ảnh tư thế (tải kèm ảnh nhân vật gốc)
```
{POSE.format(ex=ex, m=m)}
```

## Bước 2 — 3 clip chuyển động (Google Flow, dùng ảnh ở bước 1)
{clips}

## Bước 3 — Lời thoại tiếng Việt (~{len(voice.split())} từ)
```
{voice}
```
""")
print("OK: 60 file trong prompts/ + exercises.csv")
