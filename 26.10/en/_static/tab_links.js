(function () {
  "use strict";

  // Named tabs such as `:name: tab-view-layout` accept #layout, #view-layout,
  // and #tab-view-layout; unnamed tabs fall back to a slug of the visible label.
  function normalizeHash(value) {
    try {
      return decodeURIComponent(value.replace(/^#/, ""));
    } catch (error) {
      return value.replace(/^#/, "");
    }
  }

  function slugify(text) {
    var normalized = text.normalize ? text.normalize("NFKC") : text;
    var slug = "";
    var previousDash = false;

    normalized = normalized.toLowerCase().replace(/[\u25b6\u25ba\u203a>]+/g, " ");

    for (var index = 0; index < normalized.length; index += 1) {
      var char = normalized.charAt(index);
      var code = char.charCodeAt(0);
      var isAsciiLetter = code >= 97 && code <= 122;
      var isAsciiNumber = code >= 48 && code <= 57;
      var isNonAsciiText = code > 127 && !/\s/.test(char);

      if (isAsciiLetter || isAsciiNumber || isNonAsciiText) {
        slug += char;
        previousDash = false;
      } else if (!previousDash && slug.length > 0) {
        slug += "-";
        previousDash = true;
      }
    }

    slug = slug.replace(/-+$/g, "");
    return slug || "tab";
  }

  function addUnique(list, value) {
    if (value && list.indexOf(value) === -1) {
      list.push(value);
    }
  }

  function getBaseKeys(label) {
    var keys = [];
    var labelId = label.id || "";

    if (labelId.indexOf("tab-") === 0) {
      var stableKey = labelId.substring(4);
      var separatorIndex = stableKey.indexOf("-");

      if (separatorIndex !== -1) {
        addUnique(keys, stableKey.substring(separatorIndex + 1));
      }

      addUnique(keys, stableKey);
    }

    addUnique(keys, labelId);
    addUnique(keys, slugify(label.textContent || ""));

    return keys;
  }

  function getTabEntries() {
    var counts = {};
    var entries = [];
    var labels = document.querySelectorAll(".sd-tab-set > label.sd-tab-label");

    labels.forEach(function (label) {
      var input = label.previousElementSibling;

      if (!input || input.tagName.toLowerCase() !== "input") {
        return;
      }

      var aliases = getBaseKeys(label).map(function (baseKey) {
        counts[baseKey] = (counts[baseKey] || 0) + 1;
        return counts[baseKey] === 1 ? baseKey : baseKey + "-" + counts[baseKey];
      });

      entries.push({
        input: input,
        label: label,
        key: aliases[0],
        aliases: aliases
      });
    });

    return entries;
  }

  function activateFromHash(entries) {
    var hash = normalizeHash(window.location.hash);

    if (!hash) {
      return false;
    }

    for (var index = 0; index < entries.length; index += 1) {
      if (entries[index].aliases.indexOf(hash) !== -1) {
        entries[index].input.checked = true;
        entries[index].label.scrollIntoView({ block: "nearest", inline: "nearest" });
        return true;
      }
    }

    return false;
  }

  function replaceHash(key) {
    if (window.history && window.history.replaceState) {
      window.history.replaceState(null, "", "#" + encodeURIComponent(key));
    } else {
      window.location.hash = key;
    }
  }

  function ready() {
    var entries = getTabEntries();

    if (!entries.length) {
      return;
    }

    activateFromHash(entries);

    entries.forEach(function (entry) {
      entry.label.addEventListener("click", function () {
        replaceHash(entry.key);
      });
    });

    window.addEventListener("hashchange", function () {
      activateFromHash(entries);
    });
  }

  document.addEventListener("DOMContentLoaded", ready, false);
}());
