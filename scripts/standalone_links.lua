-- Used by the standalone (single-file) build only.
-- Rewrites links between chapters, e.g. [x](hsma_tech_stack.qmd) or
-- [x](hsma_tech_stack.qmd#some-heading), into in-page anchors. Each chapter is
-- wrapped in a div with id "chapter-<filename>" in HSMA-Content-Writing-Manual.qmd.

function Link(el)
  local name, fragment = el.target:match("^%.?/?([%w_%-]+)%.qmd(#?.*)$")
  if name then
    if fragment ~= "" then
      el.target = fragment
    else
      el.target = "#chapter-" .. name
    end
  end
  return el
end
