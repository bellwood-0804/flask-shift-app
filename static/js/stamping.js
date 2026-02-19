
    
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

  } catch (err) {
    alert("エラー: " + err.message);
  }
}

    // async function workout(){
    // }

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

 


    