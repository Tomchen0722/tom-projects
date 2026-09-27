/**
 * 台灣菸酒招考從業職員（資訊管理）- 交互應用程式邏輯 (App Controller)
 */

document.addEventListener("DOMContentLoaded", function () {
  'use strict';

  // 1. 考期倒數計時器
  function initCountdowns() {
    // 預設台酒招考時程 (以 115 年預估招考時程)
    var regDate = new Date("2026-10-15T09:00:00+08:00").getTime();
    var examDate = new Date("2026-11-28T08:30:00+08:00").getTime();

    function update() {
      var now = new Date().getTime();

      // 報名倒數
      var diffReg = regDate - now;
      if (diffReg > 0) {
        var d1 = Math.floor(diffReg / (1000 * 60 * 60 * 24));
        var h1 = Math.floor((diffReg % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var m1 = Math.floor((diffReg % (1000 * 60 * 60)) / (1000 * 60));
        var s1 = Math.floor((diffReg % (1000 * 60)) / 1000);

        setVal("reg-days", d1);
        setVal("reg-hours", h1);
        setVal("reg-mins", m1);
        setVal("reg-secs", s1);
      } else {
        setVal("reg-days", 0);
        setVal("reg-hours", 0);
        setVal("reg-mins", 0);
        setVal("reg-secs", 0);
      }

      // 考試倒數
      var diffExam = examDate - now;
      if (diffExam > 0) {
        var d2 = Math.floor(diffExam / (1000 * 60 * 60 * 24));
        var h2 = Math.floor((diffExam % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var m2 = Math.floor((diffExam % (1000 * 60 * 60)) / (1000 * 60));
        var s2 = Math.floor((diffExam % (1000 * 60)) / 1000);

        setVal("exam-days", d2);
        setVal("exam-hours", h2);
        setVal("exam-mins", m2);
        setVal("exam-secs", s2);
      } else {
        setVal("exam-days", 0);
        setVal("exam-hours", 0);
        setVal("exam-mins", 0);
        setVal("exam-secs", 0);
      }
    }

    function setVal(id, v) {
      var el = document.getElementById(id);
      if (el) el.textContent = v < 10 ? "0" + v : v;
    }

    update();
    setInterval(update, 1000);
  }

  // 2. 歷屆測驗互動選項點擊判斷
  function initQuizInteractive() {
    document.querySelectorAll(".quiz-item-card").forEach(function (card) {
      var correctAns = card.getAttribute("data-answer");
      var analysisBox = card.querySelector(".quiz-analysis-box");
      var buttons = card.querySelectorAll(".quiz-option-btn");

      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var userChoice = btn.getAttribute("data-opt");

          // 重置其他選項
          buttons.forEach(function (b) {
            b.classList.remove("correct", "wrong");
          });

          if (userChoice === correctAns) {
            btn.classList.add("correct");
          } else {
            btn.classList.add("wrong");
            // 標註正確選項
            buttons.forEach(function (b) {
              if (b.getAttribute("data-opt") === correctAns) {
                b.classList.add("correct");
              }
            });
          }

          if (analysisBox) {
            analysisBox.classList.add("visible");
          }
        });
      });
    });
  }

  // 3. 申論題收合與展開
  function initEssayAccordion() {
    document.querySelectorAll(".essay-q-bar").forEach(function (bar) {
      bar.addEventListener("click", function () {
        var body = bar.nextElementSibling;
        if (body && body.classList.contains("essay-a-body")) {
          var isHidden = body.style.display === "none";
          body.style.display = isHidden ? "block" : "none";
          var toggleIcon = bar.querySelector(".toggle-icon");
          if (toggleIcon) toggleIcon.textContent = isHidden ? "▲" : "▼";
        }
      });
    });
  }

  // 4. 專有名詞搜尋過濾
  function initVocabSearch() {
    var searchInput = document.getElementById("vocab-search-input");
    var filterBtns = document.querySelectorAll(".vocab-filter-btn");
    var vocabCards = document.querySelectorAll(".vocab-card");

    if (!searchInput && filterBtns.length === 0) return;

    var currentCategory = "all";

    function filterCards() {
      var query = searchInput ? searchInput.value.trim().toLowerCase() : "";

      vocabCards.forEach(function (card) {
        var cardCat = card.getAttribute("data-cat") || "all";
        var word = (card.querySelector(".vocab-word")?.textContent || "").toLowerCase();
        var full = (card.querySelector(".vocab-full-en")?.textContent || "").toLowerCase();
        var zh = (card.querySelector(".vocab-zh")?.textContent || "").toLowerCase();
        var text = (card.textContent || "").toLowerCase();

        var matchCat = currentCategory === "all" || cardCat === currentCategory;
        var matchQuery = !query || word.includes(query) || full.includes(query) || zh.includes(query) || text.includes(query);

        if (matchCat && matchQuery) {
          card.style.display = "flex";
        } else {
          card.style.display = "none";
        }
      });
    }

    if (searchInput) {
      searchInput.addEventListener("input", filterCards);
    }

    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        currentCategory = btn.getAttribute("data-cat");
        filterCards();
      });
    });
  }

  // 初始化所有模組
  initCountdowns();
  initQuizInteractive();
  initEssayAccordion();
  initVocabSearch();
});
