from governed_decisions.anti_patterns import anti_pattern_table
from governed_decisions.article_concepts import binary_classification_use_cases, decision_boundary_fit_matrix


def test_anti_pattern_table_includes_article_guidance():
    table = anti_pattern_table()

    assert {"anti_pattern", "why_it_fails", "better_practice"}.issubset(table.columns)
    assert "Always using 0.50" in table["anti_pattern"].to_list()
    assert len(table) >= 10


def test_article_concept_tables_cover_business_fit():
    use_cases = binary_classification_use_cases()
    fit_matrix = decision_boundary_fit_matrix()

    assert "Fraud monitoring" in use_cases["business_problem"].to_list()
    assert any(fit_matrix["situation"].str.contains("False positives"))
