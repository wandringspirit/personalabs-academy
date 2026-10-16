import os
import subprocess
import imageio_ffmpeg

PROJECT_DIR = r"C:\Projects\ai-influencer-course-website"
HOOKS_DIR = os.path.join(PROJECT_DIR, "instagram-studio", "05-Dancing-Hook-Options")
REEL_04 = os.path.join(PROJECT_DIR, "instagram-studio", "02-Organic-Reels", "Reel-04-Raw-iPhone-Realism-Secret-Organic.mp4")
AD_01 = os.path.join(PROJECT_DIR, "ads-ready", "01-India-INR-Ads", "Ad-01-Curiosity-Reveal-INR-9x16.mp4")
SCRATCH_DIR = os.path.join(PROJECT_DIR, "instagram-studio", ".tmp_ad04")
OUT_9X16 = os.path.join(PROJECT_DIR, "ads-ready", "01-India-INR-Ads")
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

os.makedirs(SCRATCH_DIR, exist_ok=True)
os.makedirs(OUT_9X16, exist_ok=True)

def build_full_ad_variant(hook_filename, variant_name):
    hook_path = os.path.join(HOOKS_DIR, hook_filename)
    out_file = os.path.join(OUT_9X16, f"Ad-04-{variant_name}-INR-9x16.mp4")
    print(f"\n>>> Assembling full 30s ad: {variant_name} -> {out_file}")

    # 1. Hook clip video (0 to 4.0s)
    tmp_v_hook = os.path.join(SCRATCH_DIR, f"v_hook_{variant_name}.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-t", "4.0",
        "-i", hook_path,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", "30", "-an", tmp_v_hook
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 2. Reel 04 body video (4.0s to 22.5s)
    tmp_v_body = os.path.join(SCRATCH_DIR, f"v_body_{variant_name}.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-ss", "4.0", "-to", "22.5",
        "-i", REEL_04,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", "30", "-an", tmp_v_body
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Endcard video (7.5s loop of endcard_9x16.png)
    endcard_img = os.path.join(SCRATCH_DIR, "endcard_9x16.png")
    tmp_v_end = os.path.join(SCRATCH_DIR, f"v_end_{variant_name}.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-loop", "1", "-t", "7.5",
        "-i", endcard_img,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", "30", "-an", tmp_v_end
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 4. Concat video parts
    concat_txt = os.path.join(SCRATCH_DIR, f"concat_v_{variant_name}.txt")
    with open(concat_txt, "w") as f:
        f.write(f"file '{tmp_v_hook}'\n")
        f.write(f"file '{tmp_v_body}'\n")
        f.write(f"file '{tmp_v_end}'\n")
    
    tmp_v_full = os.path.join(SCRATCH_DIR, f"v_full_{variant_name}.mp4")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy", tmp_v_full
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 5. Extract audio
    # Part 1: Reel 04 audio 0 to 22.5s
    tmp_a1 = os.path.join(SCRATCH_DIR, f"a1_{variant_name}.wav")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-ss", "0.0", "-to", "22.5",
        "-i", REEL_04,
        "-ar", "44100", "-ac", "2", tmp_a1
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Part 2: Offer CTA audio 7.5s from Ad 01
    tmp_a2 = os.path.join(SCRATCH_DIR, f"a2_{variant_name}.wav")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-ss", "23.0", "-to", "30.5",
        "-i", AD_01,
        "-ar", "44100", "-ac", "2", tmp_a2
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    concat_a_txt = os.path.join(SCRATCH_DIR, f"concat_a_{variant_name}.txt")
    with open(concat_a_txt, "w") as f:
        f.write(f"file '{tmp_a1}'\n")
        f.write(f"file '{tmp_a2}'\n")

    tmp_a_full = os.path.join(SCRATCH_DIR, f"a_full_{variant_name}.m4a")
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_a_txt,
        "-c:a", "aac", "-b:a", "192k", tmp_a_full
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 6. Mux
    subprocess.run([
        FFMPEG_EXE, "-y",
        "-i", tmp_v_full,
        "-i", tmp_a_full,
        "-c:v", "copy",
        "-c:a", "copy",
        "-movflags", "+faststart",
        "-shortest",
        out_file
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"[SUCCESS] Assembled {out_file} ({os.path.getsize(out_file):,} bytes)")

def main():
    # Build the two leading contenders
    build_full_ad_variant("Hook-Option-01-Classical-Mudra.mp4", "Classical-Mudra")
    build_full_ad_variant("Hook-Option-03-Over-Shoulder-Twirl.mp4", "Over-Shoulder")
    print("\n=== FULL AD CANDIDATES READY ===")

if __name__ == "__main__":
    main()
