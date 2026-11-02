# Enterprise and data-heavy UI

Start with the operator’s decision: identify a failing service, compare settlements, approve a batch, or recover from an error. Put the evidence for that decision together. Choose a table for row-by-row comparison, a chart for a trend, and a detail view for an individual record. Do not make users compare values across a wall of cards.

## A table that survives real data

- Keep scope visible: tenant/environment, active filters, time range and zone, count, and freshness. Provide a way to clear filters and preserve a useful return position after drilling down.
- Name units and currencies. Align comparable numbers; distinguish zero, missing, stale, and unauthorized. Make sort indicators reflect the real sort order. Clarify whether selection means visible rows, the page, or all matching results.
- Use real headers and row identifiers. A sortable table does not automatically need an ARIA grid. Preserve header/cell associations and keyboard access if virtualization is actually needed.
- Show distinct states: no records yet → creation or explanation; filters match nothing → clear filters; permission denied → access guidance; refresh failed → last known time and retry. Never turn a failed fetch into a zero balance.
- For bulk actions show target scope and operation before submission; distinguish accepted, pending, partial failure, and complete. A retry must not imply repeat execution is safe unless the API guarantees it.

## Charts, density, and responsive behavior

Show units, aggregation, time window, and source. Add text or a shape to status colors. Use realistic, non-sensitive examples for mockups. Never fabricate live status, totals, or timestamps. Keep primary identifiers and actions accessible at narrow widths; a table may have its own scroll container without causing the whole page to overflow. Test long IDs, large values, and translations. In supported themes, inspect low-contrast separators and stale/disabled states.

A useful verification: sort → filter → select rows → open a record → go Back. Check which filters, sort, page, and selections survive and whether the result still describes the same records.
