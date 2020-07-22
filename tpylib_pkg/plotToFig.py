#!/usr/bin/env python

from tpylib_FileFolderUtils import FileFolderUtils
import matplotlib.pyplot as plt
# import numpy as np


class PlotToFig:
    def __init__(self):
        pass

    @staticmethod
    def auto_lims(ax, y_arr):
        # ymin = np.min(y_arr)
        # if ymin > 0:
        #     ylower = 0.8 * ymin
        # else:
        #     ylower = 1.2 * ymin
        #
        # ymax = np.max(y_arr)
        # if ymax > 0:
        #     yupper = 1.2 * ymax
        # else:
        #     yupper = 0.8 * ymax
        #
        # ax.set_ylim([ylower, yupper])

        ax.locator_params(axis='y', nbins=3)
        ax.locator_params(axis='x', nbins=4)

    @staticmethod
    def ax1_x1_y8(ax, x, xlabel, y_arr, ylabel):
        # ax.hold(True)
        ax.grid(True)
        ax.plot(x, y_arr[0], color='red')
        ax.plot(x, y_arr[1], color='green')
        ax.plot(x, y_arr[2], color='blue')
        ax.plot(x, y_arr[3], color='black')
        ax.plot(x, y_arr[4], color='green', linestyle='dashed')
        ax.plot(x, y_arr[5], color='red', linestyle='dashed')
        ax.plot(x, y_arr[6], color='black', linestyle='dashed')
        ax.plot(x, y_arr[7], color='blue', linestyle='dashed')
        ax.set(xlabel=xlabel, ylabel=ylabel)
        # ax.ticklabel_format(useOffset=False)
        #   I was getting the error
        #   "This method only works with the ScalarFormatter.")
        #   AttributeError: This method only works with the ScalarFormatter.
        # PlotToFig.auto_lims(ax, y_arr)
        ax.locator_params(axis='y', nbins=3)
        ax.locator_params(axis='x', nbins=4)

    @staticmethod
    def ax1_x1_y4(ax, x, xlabel, y_arr, ylabel):
        # ax.hold(True)
        ax.grid(True)
        ax.plot(x, y_arr[0], color='red')
        ax.plot(x, y_arr[1], color='green')
        ax.plot(x, y_arr[2], color='blue')
        ax.plot(x, y_arr[3], color='black')
        ax.set(xlabel=xlabel, ylabel=ylabel)
        ax.ticklabel_format(useOffset=False)
        # PlotToFig.auto_lims(ax, y_arr)
        ax.locator_params(axis='y', nbins=3)
        ax.locator_params(axis='x', nbins=4)

    @staticmethod
    def ax1_x1_y3(ax, x, xlabel, y_arr, ylabel):
        # ax.hold(True)
        ax.grid(True)
        ax.plot(x, y_arr[0], color='red')
        ax.plot(x, y_arr[1], color='green')
        ax.plot(x, y_arr[2], color='blue')
        ax.set(xlabel=xlabel, ylabel=ylabel)
        ax.ticklabel_format(useOffset=False)
        # PlotToFig.auto_lims(ax, y_arr)
        ax.locator_params(axis='y', nbins=3)
        ax.locator_params(axis='x', nbins=4)

    @staticmethod
    def ax3_x1_y3(ax_arr, x, xlabel, y_arr, ylabel_arr):
        # ax_arr[0].hold(True)
        ax_arr[0].grid(True)
        ax_arr[0].plot(x, y_arr[0])
        ax_arr[0].set(xlabel=xlabel, ylabel=ylabel_arr[0])
        # PlotToFig.auto_lims(ax_arr[0], y_arr[0])
        ax_arr[0].locator_params(axis='y', nbins=3)
        ax_arr[0].locator_params(axis='x', nbins=4)

        # ax_arr[1].hold(True)
        ax_arr[1].grid(True)
        ax_arr[1].plot(x, y_arr[1])
        ax_arr[1].set(xlabel=xlabel, ylabel=ylabel_arr[1])
        # PlotToFig.auto_lims(ax_arr[1], y_arr[1])
        ax_arr[1].locator_params(axis='y', nbins=3)
        ax_arr[1].locator_params(axis='x', nbins=4)

        # ax_arr[2].hold(True)
        ax_arr[2].grid(True)
        ax_arr[2].plot(x, y_arr[2])
        ax_arr[2].set(xlabel=xlabel, ylabel=ylabel_arr[2])
        # PlotToFig.auto_lims(ax_arr[2], y_arr[2])
        ax_arr[2].locator_params(axis='y', nbins=3)
        ax_arr[2].locator_params(axis='x', nbins=4)

    @staticmethod
    def ax3_x1_y6(ax_arr, x, xlabel, y_arr, ylabel_arr):
        # ax_arr[0].hold(True)
        ax_arr[0].grid(True)
        ax_arr[0].plot(x, y_arr[0], color='red')
        ax_arr[0].plot(x, y_arr[3], color='green')
        ax_arr[0].set(xlabel=xlabel, ylabel=ylabel_arr[0])
        # PlotToFig.auto_lims(ax_arr[0], y_arr[0])
        ax_arr[0].locator_params(axis='y', nbins=3)
        ax_arr[0].locator_params(axis='x', nbins=4)

        # ax_arr[1].hold(True)
        ax_arr[1].grid(True)
        ax_arr[1].plot(x, y_arr[1], color='red')
        ax_arr[1].plot(x, y_arr[4], color='green')
        ax_arr[1].set(xlabel=xlabel, ylabel=ylabel_arr[1])
        # PlotToFig.auto_lims(ax_arr[1], y_arr[1])
        ax_arr[1].locator_params(axis='y', nbins=3)
        ax_arr[1].locator_params(axis='x', nbins=4)

        # ax_arr[2].hold(True)
        ax_arr[2].grid(True)
        ax_arr[2].plot(x, y_arr[2], color='red')
        ax_arr[2].plot(x, y_arr[5], color='green')
        ax_arr[2].set(xlabel=xlabel, ylabel=ylabel_arr[2])
        # PlotToFig.auto_lims(ax_arr[2], y_arr[2])
        ax_arr[2].locator_params(axis='y', nbins=3)
        ax_arr[2].locator_params(axis='x', nbins=4)

    @staticmethod
    def ax4_x1_y4(ax_arr, x, xlabel, y_arr, ylabel_arr):
        # ax_arr[0].hold(True)
        ax_arr[0].grid(True)
        ax_arr[0].plot(x, y_arr[0])
        ax_arr[0].set(xlabel=xlabel, ylabel=ylabel_arr[0])
        # PlotToFig.auto_lims(ax_arr[0], y_arr[0])
        ax_arr[0].locator_params(axis='y', nbins=3)
        ax_arr[0].locator_params(axis='x', nbins=4)

        # ax_arr[1].hold(True)
        ax_arr[1].grid(True)
        ax_arr[1].plot(x, y_arr[1])
        ax_arr[1].set(xlabel=xlabel, ylabel=ylabel_arr[1])
        # PlotToFig.auto_lims(ax_arr[1], y_arr[1])
        ax_arr[1].locator_params(axis='y', nbins=3)
        ax_arr[1].locator_params(axis='x', nbins=4)

        # ax_arr[2].hold(True)
        ax_arr[2].grid(True)
        ax_arr[2].plot(x, y_arr[2])
        ax_arr[2].set(xlabel=xlabel, ylabel=ylabel_arr[2])
        # PlotToFig.auto_lims(ax_arr[2], y_arr[2])
        ax_arr[2].locator_params(axis='y', nbins=3)
        ax_arr[2].locator_params(axis='x', nbins=4)

        # ax_arr[3].hold(True)
        ax_arr[3].grid(True)
        ax_arr[3].plot(x, y_arr[3])
        ax_arr[3].set(xlabel=xlabel, ylabel=ylabel_arr[3])
        # PlotToFig.auto_lims(ax_arr[3], y_arr[3])
        ax_arr[3].locator_params(axis='y', nbins=3)
        ax_arr[3].locator_params(axis='x', nbins=4)

    @staticmethod
    def savecf(filename, closefig):
        # plt.show()
        # plt.draw()

        # # Make fig the current figure
        # assert isinstance(fig, plt.figure())
        # plt.figure(fig.number)

        # Save and close current figure
        print('[savecf] filename %s' %
              FileFolderUtils.get_basename(filename))
        plt.savefig(filename, bbox_inches='tight')

        if closefig:
            plt.clf()
            plt.close()

