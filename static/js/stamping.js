
function toggle() {
      const startstamp = document.getElementById("startstamp");
      const endstamp = document.getElementById("endstamp");

      if (startstamp.style.display !== "none") {
        // 出勤 → 退勤へ
        startstamp.style.display = "none";
        endstamp.style.display = "inline";
      } else {
        // 退勤 → 出勤へ
        startstamp.style.display = "inline";
        endstamp.style.display = "none";
      }
    }

    