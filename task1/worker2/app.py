import os

DATA_FILE = "/var/data/data.txt"
RESULT_FILE = "/var/result/result.txt"

if __name__ == "__main__":
    with open(DATA_FILE, "r") as f:
        raw = f.read().split()
    nums = [int(x) for x in raw if x.strip().lstrip("-").isdigit()]

    if nums:
        mx = max(nums)
        result = mx ** 2
        with open(RESULT_FILE, "w") as f:
            f.write(str(result))
        print(f"[worker2] Max number: {mx}")
        print(f"[worker2] Max^2     : {result}")
        print(f"[worker2] Saved to  : {RESULT_FILE}")
    else:
        print("[worker2] No numbers found in data.txt")