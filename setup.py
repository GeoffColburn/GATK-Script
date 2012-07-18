#!/usr/bin/env python
from distutils.core import setup


setup(name = "GATK-Script",
      package_dir = {'':""},

      scripts = ["scripts/GATK.py"],

      data_files = [("share/gatk", ["share/gatk/GenomeAnalysisTK.jar"]),
                    ("share/picard_tools", ["share/picard_tools/AddOrReplaceReadGroups.jar",
                                            "share/picard_tools/MarkDuplicates.jar",
                                            "share/picard_tools/SortSam.jar"])]
      )#End setup.
