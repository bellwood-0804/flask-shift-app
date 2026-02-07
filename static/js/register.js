  // 前のページに戻る
document.getElementById("listback").addEventListener("click",()=>{
    window.location.href="/list"
  });

  function database() {
      fetch("/database", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
          name: document.getElementById("name").value,
          password: document.getElementById("password").value,
          hourly_wage: Number(document.getElementById("hourly_wage").value)
         })
      })
      // resは任意だがresponseの結果と分かりやすくするためにres　errもresと同じよう感じ　もしエラーが起きていたらresとerrは全く同じ値が入っている
      .then(res=>{
        if(!res.ok){
          return res.json().then(err=>{
            // .catchに投げられるための処理
            // newは新しいインスタンスを作るための処理
            throw new Error(err.message);
          });
        }
        return res.json()
      })
      // dataはres.jsonの内容が入っているこの書き方の時一つ前の処理の中身の内容を参照
       .then(data => {
    alert(data.message);
    loadList(); // ← 登録後に一覧更新
  })
  .catch(err => {
    alert("エラー: " + err.message);
  });
}

// 削除ボタンを押したときの処理
document.getElementById("delete-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  // チェックされている checkbox を全部取得
  // arrayは配列にしている　。mapはある配列を違う配列に置き換えること、今回はvalue要素だけを取り出す処理
  const checkedUsers = Array.from(
    document.querySelectorAll('input[name="staff"]:checked')
  ).map(cb => cb.value);

  const res = await fetch("/delete", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      ids: checkedUsers
    })
  })
   .then(res=>{
        if(!res.ok){
          return res.json().then(err=>{
            throw new Error(err.message);
          });
        }
        return res.json()
      })
    .then(data => {
    alert(data.message);
    loadList(); // ← 登録後に一覧更新
  })
  .catch(err => {
    alert("エラー: " + err.message);
  });    
});


 
    function loadList() {
    fetch("/database/list")
    .then(res => res.json())
    .then(data => {
      // このlistはhtmlにある要素を取得しているだけ
        const ul = document.getElementById("list");
        ul.innerHTML = "";
        // foreachは配列の中を一つずつ取り出して処理する
        // itemは配列の中にある一件分のデータ
        data.forEach(item => {
          // liはhtmlの構文のこと
            const li =document.createElement("li")
            // <input type="checkbox" のことと同義　inputというタグを作って実際にtypeは何かと書いている
            const input = document.createElement("input");
              input.type = "checkbox";
              input.name = "staff";        // ← 削除対象
              input.value = item.id; 
                 // 追加情報は data-* に保持
                //  今のところdatasetはいらない
              input.dataset.name = item.name;
              input.dataset.hourlyWage = item.hourly_wage;
                const text = document.createTextNode(
              ` ${item.id} ${item.name} （${item.hourly_wage}円）`
                );
            li.appendChild(input);
            li.appendChild(text);
            ul.appendChild(li);
        });
    });
}

// ページロード時に一覧を取得
loadList();
