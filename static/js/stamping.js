
function toggle() {
      const startstamp = document.getElementById("startstamp");
      const endstamp = document.getElementById("endstamp");

      if (startstamp.style.display !== "none") {
        // 出勤 → 退勤へ
        startstamp.style.display = "none";
        endstamp.style.display = "inline";
        workin();
        // 出勤打刻を押した場合
      } else {
        // 退勤 → 出勤へ
        startstamp.style.display = "inline";
        endstamp.style.display = "none";
        workout()
      }
    }

    // 出勤時の処理
    
    async function workin() {
  try {
    const token = localStorage.getItem("token");

    const res = await fetch("/clock_in", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.message);
    }

    const data = await res.json();
    alert(data.message);
    loadList();

  } catch (err) {
    alert("エラー: " + err.message);
  }
}

    async function workout(){
     loginname()
    }

  //    async function loginname() {
  //     const token = localStorage.getItem("token")

  //   const res = await fetch("/list/api/me", {
  //     // jwtお決まりの文言でこの人がログインした人ですという認証
  //   headers: {
  //   Authorization: `Bearer ${token}`
  //  }
  // });

  //     const data = await res.json();
  //   }

 


    